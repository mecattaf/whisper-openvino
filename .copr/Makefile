.PHONY: srpm prepare

BUILDDIR := $(shell pwd)
SPECFILE := $(spec)

prepare:
	# First install dnf plugins and basic build tools
	dnf install --nodocs -y 'dnf-command(config-manager)' rpm-build rpmdevtools
	# Copy and enable OpenVINO repo
	cp $(dir $(SPECFILE))/openvino-2024.repo /etc/yum.repos.d/
	dnf config-manager --add-repo /etc/yum.repos.d/openvino-2024.repo
	# Import OpenVINO GPG key
	rpm --import https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB
	# Update repo metadata
	dnf makecache
	# Now install build dependencies
	dnf install --nodocs -y \
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
