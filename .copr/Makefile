.PHONY: srpm prepare

BUILDDIR := $(shell pwd)
SPECFILE := $(spec)

prepare:
	# First install basic build tools (skip ones that are already installed)
	dnf5 install --nodocs -y --setopt=strict=0 rpmdevtools \
		cmake clang gcc-c++ make \
		openblas-devel
	# Copy OpenVINO repo and import key
	cp $(dir $(SPECFILE))/openvino-2024.repo /etc/yum.repos.d/
	rpm --import https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB
	# Update metadata and install OpenVINO
	dnf5 makecache
	dnf5 install --nodocs -y openvino

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
