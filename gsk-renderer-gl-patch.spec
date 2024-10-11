Name: gsk-renderer-gl-patch
Summary: Patch for GSK rendering issues (sets GSK_RENDERER=gl)
Version: 1.0.4
Release: 1%{?dist}
License: unlicense
Group: System/Configuration/Files
Requires: sed

%description
Patch for GSK rendering issues (sets GSK_RENDERER=gl)

%install
install -D -m 0544 src/main.sh %{_bindir}/gsk-renderer-gl-patch
install -D -m 0544 lib/set.sh %{_libdir}/gsk-renderer-gl-patch/set.sh
install -D -m 0544 lib/revert.sh %{_libdir}/gsk-renderer-gl-patch/revert.sh
install -D -m 0544 lib/reboot.sh %{_libdir}/gsk-renderer-gl-patch/reboot.sh
install -D -m 0544 lib/variables.sh %{_libdir}/gsk-renderer-gl-patch/variables.sh

%files
%{_bindir}/gsk-renderer-gl-patch
%{_libdir}/gsk-renderer-gl-patch/set.sh
%{_libdir}/gsk-renderer-gl-patch/revert.sh
%{_libdir}/gsk-renderer-gl-patch/reboot.sh
%{_libdir}/gsk-renderer-gl-patch/variables.sh

%post
gsk-renderer-gl-patch set

%preun
gsk-renderer-gl-patch revert

%changelog
* Fri Oct 11 2024 Malix <alixbrunetcontact@gmail.com> 1.0.4-1
- yes test tito

* Fri Oct 11 2024 Malix-off <alixbrunetcontact@gmail.com> 1.0.3-1
- enhance: change perm (alixbrunetcontact@gmail.com)

* Fri Oct 11 2024 Malix <alixbrunetcontact@gmail.com>
- new package built with tito
