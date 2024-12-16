prepare:
	# Set up OpenVINO repository first
	cat $(dir $(SPECFILE))/openvino-2024.repo > /etc/yum.repos.d/openvino.repo
	chmod 644 /etc/yum.repos.d/openvino.repo
	
	# Debug: Show repo file
	echo "=== OpenVINO repo file content ==="
	cat /etc/yum.repos.d/openvino.repo
	
	# Debug: List all repo files
	echo "=== All repo files ==="
	ls -la /etc/yum.repos.d/
	
	# Import key
	rpm --import https://yum.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS.PUB
	
	# Debug: Check repo availability
	echo "=== Testing repo access ==="
	curl -v https://yum.repos.intel.com/openvino/2024/repodata/repomd.xml || true
	
	# Clean and refresh repository metadata
	dnf5 clean all
	dnf5 makecache --refresh
	
	# Debug: Show all enabled repos
	echo "=== Enabled repositories ==="
	dnf5 repolist enabled
	
	# Debug: Show all repos including disabled
	echo "=== All repositories ==="
	dnf5 repolist all
	
	# List available OpenVINO packages
	echo "=== OpenVINO packages ==="
	dnf5 list 'openvino*' || true
	
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
