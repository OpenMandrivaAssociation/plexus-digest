%{?_javapackages_macros:%_javapackages_macros}

%global parent plexus
%global subname digest

Name:           plexus-digest
Version:        1.1
Release:        16.2
Epoch:          0
Summary:        Plexus Digest / Hashcode Components
Group:		Development/Java
License:        ASL 2.0

URL:            https://plexus.codehaus.org/plexus-components/plexus-digest/
Source0:        %{name}-%{version}-src.tar.gz
# svn export http://svn.codehaus.org/plexus/plexus-components/tags/plexus-digest-1.1/ plexus-digest/
# tar czf plexus-digest-1.1-src.tar.gz plexus-digest/

Patch0:         %{name}-migration-to-component-metadata.patch
Patch1:         %{name}-fix-test-dependencies.patch
Patch2:         0001-Do-not-use-algorithm-name-as-regular-expression.patch

BuildArch:      noarch

BuildRequires:	junit
BuildRequires:  maven-local
BuildRequires:  plexus-containers-component-metadata


%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%package javadoc
Summary:        Javadoc for %{name}


%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%pom_add_dep junit:junit::test

%build
%mvn_file  : plexus/digest
%mvn_build

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Sep 27 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 0:1.1-14
- Do not use algorithm name as regular expression
- Resolves: rhbz#959454

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 08 2013 Michal Srb <msrb@redhat.com> - 0:1.1-12
- Remove unnecessary BR on maven-doxia and maven-doxia-sitetools

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 0:1.1-11
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 0:1.1-10
- Build with xmvn

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 22 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.1-8
- Fix test dependencies

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0:1.1-6
- Rebuild for java 1.6.0 downgrade (fesco ticket 663)

* Tue Jul 26 2011 Jaromir Capik <jcapik@redhat.com> - 0:1.1-5
- Migration from plexus-maven-plugin to plexus-containers-component-metadata
- Minor spec file changes according to the latest guidelines

* Sun Jun 12 2011 Alexander Kurtakov <akurtako@redhat.com> 0:1.1-4
- Build with maven 3.x

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 8 2010 Alexander Kurtakov <akurtako@redhat.com> 0:1.1-2
- Drop ant build.
- Adapt to new guidelines.

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.1-1
- Update to upstream 1.1.

* Tue Dec 22 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-10
- Drop not needed depmap.
- Build with maven.

* Fri Aug 21 2009 Alexander Kurtakov <akurtako@redhat.com> 0:1.0-9
- Fix License, formatting and comments.

* Sun May 17 2009 Fernando Nasser <fnasser@redhat.com> 0:1.0-8
- Fix license

* Tue Apr 30 2009 Yong Yang <yyang@redhat.com> 1.0-7
- Rebuild with new maven2 2.0.8 built in non-bootstrap mode

* Tue Apr 30 2009 Yong Yang <yyang@redhat.com> 1.0-6
- force to BR plexus-cdc alpha 10
- rebuild without maven

* Tue Apr 30 2009 Yong Yang <yyang@redhat.com> 1.0-5
- Add BRs maven-doxia*, qdox
- Enable jpp-depmap
- Rebuild with new maven2 2.0.8 built in non-bootstrap mode
- ignore test failure

* Tue Mar 17 2009 Yong Yang <yyang@redhat.com> 1.0-4
- rebuild with new maven2 2.0.8 built in bootstrap mode

* Thu Feb 05 2009 Yong Yang <yyang@redhat.com> 1.0-3
- Fix release tag

* Wed Jan 14 2009 Yong Yang <yyang@redhat.com> 1.0-2jpp.1
- Import from dbhole's maven 2.0.8 packages, initial building

* Mon Jan 07 2008 Deepak Bhole <dbhole@redhat.com> 1.0-1jpp.1
- Import from JPackage
- Update per Fedora spec

* Wed Nov 14 2007 Ralph Apel <r.apel @ r-apel.de> - 0:1.0-1jpp
- Initial build
