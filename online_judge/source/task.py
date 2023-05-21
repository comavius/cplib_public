import subprocess
import os
import uuid

class Task_gcc:
    
    def __init__(self, url: str, tempfile_dir: str, editing_path: str, lib_path: str, edittemp_path: str):
        self.url = url
        self.id = uuid.uuid4()
        self.testcase_path = tempfile_dir + '/' + str(self.id) + '/testcase'
        self.submission_path = tempfile_dir + '/' + str(self.id) + '/submission.cpp'
        self.exe_path = tempfile_dir + '/' + str(self.id) + '/executable.out'
        self.editing_path = editing_path
        self.is_accepted = False
        os.mkdir(tempfile_dir + '/' + str(self.id))
        os.mkdir(self.testcase_path)
        self.__make_editing_file(edittemp_path)
        self.lib = self.__read_libfile(lib_path)
        self.__download_testceses()

    #for encapsulation
    def get_id(self):
        return self.id

    #for encapsulation
    def get_url(self):
        return self.url
    
    def __make_editing_file(self, edittemp_path: str) -> None:
        edittemp = str()
        with open(edittemp_path, mode='r') as file:
            edittemp = file.read()
        with open(self.editing_path, mode='w') as file:
            file.write(edittemp)
    
    #for initialization
    def __download_testceses(self):
        self.__establish_bash()
        if (not(os.path.exists(self.testcase_path))):
            os.mkdir(self.testcase_path)
        self.bash.stdin.write(('oj d ' + self.url + ' -d ' + self.testcase_path + '\n').encode())
        stdout, stderr = self.bash.communicate()
    
    #for each editing file change
    def test(self) -> bool:
        self.__establish_bash()
        self.bash.stdin.write(('g++ -std=c++14 -o ' + self.exe_path + ' ' + self.submission_path + '\n').encode())
        self.bash.stdin.write(('oj t -d ' + self.testcase_path + ' -c ' +  self.exe_path + '\n').encode())
        stdout, stderr = self.bash.communicate()
        print(stdout.decode())
        return True
    
    def submit(self) -> None:
        self.__establish_bash()
        self.bash.stdin.write(('oj login ' + self.url + '\n').encode())
        print(self.submission_path)
        self.bash.stdin.write(('oj s ' + self.url + ' ' + self.submission_path + ' -y -l gcc\n').encode())
        stdout, stderr = self.bash.communicate()
        print(stdout.decode())

    #for each editing file change
    def marge(self) -> None:
        mainfunc = str()
        with open(self.editing_path, mode='r') as file:
            is_in_main = False
            for line in file:
                if (line.find('main(') != -1):
                    is_in_main = True
                if (is_in_main):
                    mainfunc += line
        with open(self.submission_path, mode='w') as file:
            file.write(self.lib)
            file.write(mainfunc)

    #for initialization        
    def __read_libfile(self, lib_path: str) -> str:
        print(lib_path)
        with open(lib_path, mode='r') as file:
            return file.read()
    
    #for oj manipulation
    def __establish_bash(self):
        self.bash = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
