.PHONY: srpm prepare

BUILDDIR := $(shell pwd)
SPECFILE := $(spec)

prepare:
	# First install dnf plugins and basic build tools
	dnf5 install --nodocs -y 'dnf5-command(config-manager)' rpm-build rpmdevtools
	# Copy and enable OpenVINO repo
	cp $(dir $(SPECFILE))/openvino-2024.repo /etc/yum.repos.d/
	# Instead of config-manager, we'll just use the copied repo directly and refresh
	# Update repo metadata 
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
