# COPR Build Automation for whisper-openvino

This repository contains automation for building the whisper-openvino package in Fedora COPR. The package provides OpenVINO-enabled builds of whisper.cpp optimized for Intel processors.

## Workflows

### Build (.github/workflows/build.yml)
- Triggers on:
  - Manual workflow dispatch
  - Push events affecting spec files or workflow configurations
- Builds package for:
  - Fedora 41
  - Fedora Rawhide
- Architecture: x86_64 only

### Update (.github/workflows/update.yml)
- Checks for new whisper.cpp releases twice daily
- Updates spec file and source hash automatically
- Triggers rebuild when updates are found

## Setup Requirements

1. Configure COPR repository:
   - Enable OpenVINO repository in COPR project settings
   - Add `openvino-2024.repo` to project configuration

2. GitHub Secrets:
   - `COPR_CONFIG`: Your COPR configuration file contents

## Build Dependencies
- cmake >= 3.27
- clang
- gcc-c++
- openvino-runtime-devel
- openblas-devel

## Package Features
- OpenVINO acceleration support
- OpenBLAS optimization
- AVX and F16C instruction set support
- Optimized for modern Intel processors

## Credit and Attribution
- The OpenVINO integration approach and optimization flags are based on the excellent work done by mkiol in the DSNote (Speech Note) Flatpak application (https://github.com/mkiol/dsnote). Their implementation demonstrated the successful integration of OpenVINO with whisper.cpp in a production environment.
- Official rpms from Tom Rix:
    - https://src.fedoraproject.org/rpms/whisper-cpp/blob/rawhide/f/0001-Generalize-install-locations.patch
    - https://src.fedoraproject.org/rpms/whisper-cpp/blob/rawhide/f/sources
    - https://src.fedoraproject.org/rpms/whisper-cpp/tree/rawhide
    - https://src.fedoraproject.org/rpms/whisper-cpp/blob/rawhide/f/whisper-cpp.spec
- COPR repo from man2dev: 
    - https://copr.fedorainfracloud.org/coprs/man2dev/whisper-cpp/build/7531134/
    - https://copr-dist-git.fedorainfracloud.org/cgit/man2dev/whisper-cpp/whisper-cpp.git/tree/whisper-cpp.spec?h=f40&id=15176c5d447e2f914aca9960d4c790ead697830b
    - https://copr-dist-git.fedorainfracloud.org/cgit/man2dev/whisper-cpp/whisper-cpp.git/diff/whisper-cpp.spec?h=f40&id=15176c5d447e2f914aca9960d4c790ead697830b

And of course the [official whisper-cpp repo](https://github.com/ggerganov/whisper.cpp)


