.PHONY: srpm prepare

BUILDDIR := $(shell pwd)
SPECFILE := $(spec)

prepare:
	dnf install --nodocs -y rpm-build rpmdevtools \
		cmake clang gcc-c++ make \
		openvino-runtime-devel openvino-runtime \
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
