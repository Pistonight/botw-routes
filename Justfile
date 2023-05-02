set windows-shell:= ["powershell", "-NoLogo", "-Command"]

build:
    just projects/adx/build
    just projects/as26/build
    just projects/as32/build
    just projects/as33/build
    just projects/akm/build
    just projects/aq/build
    just projects/aq2/build
    just projects/as4/build
    just projects/msr/build
