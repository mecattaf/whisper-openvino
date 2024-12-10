Name:           whisper-openvino
Version:        1.7.2
Release:        1%{?dist}
Summary:        OpenVINO-enabled build of whisper.cpp speech recognition

License:        MIT
URL:            https://github.com/ggerganov/whisper.cpp
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/whisper.cpp-%{version}.tar.gz
Source1:        openvino-2024.repo
Patch0:         0001-Generalize-install-locations.patch

ExclusiveArch:  x86_64
%global toolchain clang

# Base build requirements from whisper-cpp
BuildRequires:  cmake >= 3.27
BuildRequires:  clang
BuildRequires:  gcc-c++
BuildRequires:  make

# OpenVINO requirements
BuildRequires:  openvino-runtime-devel
BuildRequires:  openvino-runtime

# OpenBLAS for better performance
BuildRequires:  openblas-devel

Requires:       openvino-runtime
Requires:       openblas

# Conflicts with base whisper-cpp package
Conflicts:      whisper-cpp

%description
High-performance inference of OpenAI's Whisper automatic speech recognition (ASR) 
model, optimized with Intel's OpenVINO toolkit. This build includes:

* OpenVINO acceleration support for Intel CPUs and GPUs
* OpenBLAS optimization
* AVX and F16C instruction set support
* Optimized for modern Intel processors

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      whisper-cpp-devel

%description devel
Development files for %{name}, including headers and libraries needed
to build applications using whisper-cpp with OpenVINO support.

%prep
# Setup Intel OpenVINO repository
mkdir -p %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/yum.repos.d/

%autosetup -p1 -n whisper.cpp-%{version}

# Version the ggml *.so
sed -i -e 's@POSITION_INDEPENDENT_CODE ON@POSITION_INDEPENDENT_CODE ON SOVERSION ${SOVERSION}@' ggml/src/CMakeLists.txt

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DWHISPER_OPENVINO=ON \
    -DGGML_NATIVE=OFF \
    -DGGML_BLAS=ON \
    -DGGML_BLAS_VENDOR=OpenBLAS \
    -DGGML_AVX=ON \
    -DGGML_AVX2=OFF \
    -DGGML_FMA=OFF \
    -DGGML_F16C=ON \
    -DBUILD_SHARED_LIBS=ON \
    -DWHISPER_BUILD_TESTS=OFF \
    -DWHISPER_BUILD_EXAMPLES=OFF \
    -DCMAKE_C_FLAGS="-O3" \
    -DCMAKE_CXX_FLAGS="-O3"

%cmake_build

%install
%cmake_install

%files
%license LICENSE
%{_sysconfdir}/yum.repos.d/openvino-2024.repo
%{_libdir}/libggml.so.*
%{_libdir}/libwhisper.so.*

%files devel
%doc README.md
%{_includedir}/ggml*.h
%{_includedir}/whisper.h
%{_libdir}/libggml.so
%{_libdir}/libwhisper.so
%{_libdir}/cmake/whisper/*.cmake

%changelog
* Mon Dec 09 2024 Your Name <thomasmecattaf@gmail.com> - 1.7.2-1
- Update to version 1.7.2
- Initial package with OpenVINO support
