.PHONY: srpm prepare

BUILDDIR := $(shell pwd)
SPECFILE := $(spec)

prepare:
	# Install build requirements
	dnf5 install --nodocs -y --setopt=strict=0 \
		cmake clang gcc-c++ make \
		rpmdevtools \
		openblas-devel
	# Set up OpenVINO repository 
	cat $(dir $(SPECFILE))/openvino-2024.repo > /etc/yum.repos.d/openvino.repo
	chmod 644 /etc/yum.repos.d/openvino.repo
	rpm --import https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB
	dnf5 clean all
	dnf5 makecache --refresh
	# Install OpenVINO
	dnf5 install --nodocs -y --setopt=strict=0 openvino

srpm: prepare
	cd $(dir $(SPECFILE)) && spectool -g $(notdir $(SPECFILE))
	rpmbuild -bs \
		--define "_sourcedir $(dir $(SPECFILE))" \
		--define "_specdir $(dir $(SPECFILE))" \
		--define "_builddir $(BUILDDIR)" \
		--define "_srcrpmdir $(outdir)" \
		--define "_rpmdir $(BUILDDIR)" \
		--define "_buildrootdir $(BUILDDIR)/.build" \
		$(SPECFILE)
