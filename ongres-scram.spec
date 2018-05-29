Name:		ongres-scram
Version:	1.0.0~beta.2
Release:	1%{?dist}
Summary:	Salted Challenge Response Authentication Mechanism (SCRAM) - Java Implementation
License:	BSD
URL:		https://github.com/ongres/scram
Source0:	https://github.com/ongres/scram/archive/1.0.0-beta.2.tar.gz
BuildRequires:	maven-local
BuildArch:	noarch

%description
This is a Java implementation of SCRAM (Salted Challenge Response
Authentication Mechanism) which is part of the family of Simple
Authentication and Security Layer (SASL, RFC 4422) authentication
mechanisms. It is described as part of RFC 5802 and RFC7677.

%package client
Summary:	Client for %{name}

%description client
This package contains the client for %{name}

%package javadoc
Summary:	Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}

%package parent
Summary:	Parent POM of %{name}

%description parent
This package contains the %{name} parent POM.

%prep
%setup -q -n scram-1.0.0-beta.2
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-dependency-plugin client

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-common
%license LICENSE

%files client -f .mfiles-client
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%files parent -f .mfiles-parent
%license LICENSE

%changelog
* Fri Nov 24 2017 Augusto Caringi <acaringi@redhat.com> 1.0.0~beta.2-1
- initial rpm
