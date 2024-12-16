.PHONY: srpm prepare

BUILDDIR := $(shell pwd)
SPECFILE := $(spec)

prepare:
	# Debug: Show paths and current directory
	pwd
	ls -la
	
	# Set up OpenVINO repository first
	cat "$(dir $(SPECFILE))/openvino-2024.repo" > /etc/yum.repos.d/openvino.repo
	chmod 644 /etc/yum.repos.d/openvino.repo
	
	# Debug: Verify repo file
	echo "=== Repo file contents ==="
	ls -l /etc/yum.repos.d/
	cat /etc/yum.repos.d/openvino.repo
	
	# Import GPG key
	rpm --import https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB
	
	# Debug: Show configured repos
	echo "=== Configured repositories ==="
	dnf5 repolist
	
	# Clean and refresh repository metadata
	dnf5 clean all
	dnf5 makecache --refresh
	
	# List available OpenVINO packages
	echo "=== Available OpenVINO packages ==="
	dnf5 list --all 'openvino*' || true
	
	# Install build requirements
	dnf5 install --nodocs -y --setopt=strict=0 \
		cmake clang gcc-c++ make \
		rpmdevtools \
		openblas-devel \
		openvino-devel \
		openvino

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
