from fabric.api import local

def update():
    local('wget https://github.com/FortAwesome/Font-Awesome/raw/master/fonts/FontAwesome.otf -O FontAwesome.otf')

    local('wget https://github.com/FortAwesome/Font-Awesome/raw/master/src/icons.yml -O icons.yml')
    file = open('icons.yml', 'r')
    data = file.read()
    file.close()
    local('rm icons.yml')

    import yaml
    icons = yaml.load(data)['icons']
    str = ''
    for icon in icons:
        str += '"{0}": "\u{{{1}}}",\n'.format(icon['id'], icon['unicode'])
    swift_code = """icons = [
{0}
]""".format(str[0:-2])
    swift_file = open('FontAwesome.swift', 'w')
    swift_file.write(swift_code)
    swift_file.close()
