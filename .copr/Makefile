.PHONY: srpm prepare

BUILDDIR := $(shell pwd)
SPECFILE := $(spec)

prepare:
	# First install basic build tools
	dnf5 install --nodocs -y rpm-build rpmdevtools dnf5-plugins-core
	# Copy OpenVINO repo and import key
	cp $(dir $(SPECFILE))/openvino-2024.repo /etc/yum.repos.d/
	rpm --import https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB
	# Update metadata
	dnf5 makecache
	# Now install build dependencies
	dnf5 install --nodocs -y \
		cmake clang gcc-c++ make \
		openvino \
		openblas-devel

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
