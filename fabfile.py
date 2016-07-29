from fabric.api import local, env, run, put, cd, task, lcd, path
from fabric.contrib import project

from sparkutil import sparkfab as s


from fabric.api import local, env, run, put, cd, task
from fabric.contrib import project
import fabric as fab

from sparkutil import sparkfab as s

env.roledefs['m'] = ['jonas@c65']

@task
def deploy():
        local('git ls-tree --full-tree --name-only -r HEAD > .git-files-list')
    
        project.rsync_project("/data/jonas/neuroproc.data/", local_dir="./",
                              exclude=['*.npy', "*.ipynb", 'data'],
                              extra_opts='--files-from=.git-files-list')

        project.rsync_project("/data/jonas/neuroproc.data/",
                              local_dir=".",
                              extra_opts="--include '*.png' --include '*.pdf' --include '*.ipynb'  --include='*/' --exclude='*' " ,
                              
                              upload=False)
    
