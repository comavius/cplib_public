import uuid
import os
from source import task

class Contest:
    
    taskdict = {
        'abc': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
        'arc': ['a', 'b', 'c', 'd', 'e', 'f'],
        'agc': ['a', 'b', 'c', 'd', 'e', 'f']
    }
    
    urldict = {
        'abc': lambda contest, task: 'https://atcoder.jp/contests/' + contest + '/tasks/' + contest + '_' + task,
        'arc': lambda contest, task: 'https://atcoder.jp/contests/' + contest + '/tasks/' + contest + '_' + task,
        'agc': lambda contest, task: 'https://atcoder.jp/contests/' + contest + '/tasks/' + contest + '_' + task
    }
    
    def __init__(self, repo_path: str, type: str, contest_number: str):
        self.id = uuid.uuid4()
        self.contest_name = type + contest_number
        self.repo_path = repo_path
        self.temp_path = repo_path + '/temp/' + str(self.id)
        self.lib_path = self.temp_path + '/lib.cpp'
        os.mkdir(self.temp_path)
        #edit template
        self.edittemp_path = self.repo_path + '/lib/edittemp.cpp'
        self.get_edittemp()
        self.get_libs()
        self.set_tasks(type, self.temp_path, self.lib_path)
        

    def set_tasks(self, type: str, tempfile_dir: str, lib_path: str):
        self.tasks = {}
        for i in self.taskdict[type]:
            edit_path = self.repo_path + '/edit/' + i + '.cpp'
            self.tasks[i] = task.Task_gcc(self.urldict[type](self.contest_name, i), tempfile_dir, edit_path, lib_path, self.edittemp_path)

    def get_libs(self):
        lib = str()
        with open(self.repo_path + '/lib/list.csv') as file:
            for libname in file:
                libname = libname.rstrip()
                with open(self.repo_path + '/lib/' + libname + '/' + libname + '.cpp') as libfile:
                    lib += libfile.read()
        with open(self.lib_path, mode='w') as file:
            file.write(lib + "\n")
    
    def get_edittemp(self):
        with open(self.edittemp_path, mode='w') as file:
            file.write('#include ' + '"' + self.repo_path + '/lib/cplib_main.hpp"\n')
            file.write('using namespace std;\n')
            file.write('using namespace cplib;\n\n')
            file.write('int main() {\n    \n    return 0;\n}\n')

    def test(self, task_name: str) -> None:
        self.tasks[task_name].test()
    
    def marge(self, task_name: str) -> None:
        self.tasks[task_name].marge()
    
    def submit(self, task_name: str) -> None:
        self.tasks[task_name].submit()
