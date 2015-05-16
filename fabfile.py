from fabric.api import local

def update():
    local('rm -f FontAwesome.otf')
    local('wget https://github.com/FortAwesome/Font-Awesome/raw/master/fonts/FontAwesome.otf')
