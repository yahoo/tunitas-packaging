# Tunitas Packaging

The repository contains packaging and release machinery for the _Tunitas_ projects.
Specifically, the packaging is for Red Hat-sphere RPM packaging on (modern) RHEL and (modern) Fedora systems.

This repository also contains the common documentation for the project family as a whole resides here in the packaging repository.  As such, this repository consists mostly of documentation and the configuration files necessary to create the RPM-based packages. This use of _packaging as the default central area_ is also described in the summary documentation for each of the projects in the Tunitas family, The declarations and definitions of dependencies and requirements in this packaging repository are expected to be sufficient and complete.  They should be interpreted as superceding any statements in an individual Tunitas project when the two are in conflict (though of course there should be no conflicting statements at all!)  In certain cases, such as database choices or build tooling, more more detailed documentation may be found in the project itself.  That will be clear from the context. For example [Temerarious Flagship](https://github.com/yahoo/temerarious-flagship) can reasonably be expected to have more detailed documentation on compiler and build toolchain dependencies whereas this packaging repository can be expected to have more authoritative documentation on package dependencies.

Current work with modern-generation tooling, <em>e.g.</em> circa Fedora 36+ and GCC 12+, is occurring around the <em>thematic</em> themed branches; <em>e.g.</em> 01.famous-oak, 02.towering redwood, 03.gnarled-manzanita, and so forth.
## Table of Contents

- [Background](#background)
- [Presentation](#presentation)
- [Dependencies](#dependencies)
- [Structure](#structure)
- [Configuration](#configuration)
- [Build](#build)
- [Security](#security)
- [Contribute](#contribute)
- [License](#license)
- [Origin of the Names](#Origin_of_the_names)
- [The Family of Projects](#The_family_of_projects)

## Background

The Tunitas family of technologies provide reference implementations for a number of advertising-related services.  Several of these are well-known capabilities for which there are no open source reference implementations. An example of this first category is [Tuintas Butano](https://github.com/yahoo/tunitas-butano) which provides a reference implementation of the Interactive Advertising Bureau's (IAB) [Transparency and Consent Framework (TCF)](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework).  Other repositories provide reference implementations to advanced or experimental or capabilities. The project [Tunitas Scarpet](https://github.com/yahoo/tunitas-scarpet) provides a reference implementation of the so called [Self-Sovereign Identity (SSI)](https://sovrin.org/faq/what-is-self-sovereign-identity/) based upon the W3C's [Distributed Identity Specification](https://w3c-ccg.github.io/did-spec/).  The project [Tujnitas Apanolio](https://github.com/yahoo/tunitas-apanolio) and [Tunitas-Montara](https://github.com/yahoo/tunitas-montara) provide a reference implementation of the North-Facing Service ("Nortbound API") of the IAB's [PrivacyChain](https://github.com/InteractiveAdvertisingBureau/PrivacyChain) specification.  The other repositories in the Tunitas family provide incidental support for these and other capabilities.

## Presentation

The packaging provided here is centered around RPM-based systems such as as Red Hat or Fedora.  This is not a requirement of the system, but rather a convenience to establish the early releases of the project.  It is (and would be) straightforward to extend this system to support DEB-based packaging systems or to modern container-based distribution mechanisms.  Perhaps these features are something _you_ could contribute in a [pull request](https://github.com/yahoo/tunitas-packaging/blob/master/Contributing.md).

There are a number of delivery schemes that can be envisioned

    * RPM (RHEL, CentOS & Fedora)
    * DEB (Debian & Ubuntu)
    * Docker (is popular these days)
    * Kubernetes (is also popular)

Only rpm is implemented at this point.

## Dependencies

The dependencies of the Tunitas family of projects is documented in the `dependencies` directory and in the per-repository `PACKAGES.md` file.

Generally, the dependencies are among:
- Certain other components of the Tunitas system; <em>e.g.</em> the [Basic Components](https://github.com/yahoo/tunitas-basic).
- A modern (C++2a) development environment.
- A recent Fedora, but any recent Linux distro should suffice.

The Tunitas project was developed on Fedora 27 through Fedora 30 using GCC 7 and GCC 8 with `-fconcepts` and at least `-std=c++1z`.  More details on the development environment and the build system can be found in [temerarious-flagship](https://github.com/yahoo/temerarious-flagship/blob/master/README.md).

## Structure

The packaging repository is considered to be a unifying "top" of the Tunitas famiy of projects.  The packaging repository incorporates each of the individual projects as a git submodule.  Once the repository clone is initialized, the individual projects appear within the tree.

### Submodules

In a development context, is also envisioned that this packaging repository form the top of a tree with the individual components being linked in through the git submdoules system.  The documentation [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) documentation provides more explanation than is sketched herein.

### Directory Layout

* `dependencies`
  * [Fedora.list](https://github.com/yahoo/tunitas-packaging/blob/master/dependencies/Fedora.list) - Standard Fedora packages
  * [nonstd.list](https://github.com/yahoo/tunitas-packaging/blob/master/dependencies/nonstd.list) - Non-Standard packaging of Standard Fedora, <em>i.e.</em> patches.
  * [Tunitas.list](https://github.com/yahoo/tunitas-packaging/blob/master/dependencies/Tunitas.list) - Tunitas core components
* `rpms`
  * [Makefile](https://github.com/yahoo/tunitas-packaging/blob/master/rpms/Makefile) - rpm building
  * [temerarious-flagship.spec](https://github.com/yahoo/tunitas-packaging/blob/master/rpms/temerarious-flagship.spec) - The Build System
  * [tunitas-basics.spec](https://github.com/yahoo/tunitas-packaging/blob/master/rpms/tunitas-basics.spec) - Basic Components
  * [tunitas-butano.spec](https://github.com/yahoo/tunitas-packaging/blob/master/rpms/tunitas-butano.spec) - Components for IAB Transparency & Consent Framework (TCF)
  * [tunitas-apanolio.spec](https://github.com/yahoo/tunitas-packaging/blob/master/rpms/tunitas-apanolio.spec) - A "North-Facing Service" of PrivacyChain as a macroservice
  * [tunitas-montara.spec](https://github.com/yahoo/tunitas-packaging/blob/master/rpms/tunitas-montara.spec) - A "North-Facing Service" of PrivacyChain as a microservice
  * [tunitas-scarpet.spec](https://github.com/yahoo/tunitas-packaging/blob/master/rpms/tunitas-scarpet.spec) - Self Sovereign Identity, a W3C DID Resolver and Certificate Authority
* `sources` which are the submodules
  * [apanolio](https://github.com/yahoo/tunitas-apanolio)
  * [basics](https://github.com/yahoo/tunitas-basics)
  * [butano](https://github.com/yahoo/tunitas-butano)
  * [montara](https://github.com/yahoo/tunitas-montara)
  * [rockaway](https://github.com/yahoo/tunitas-rockaway)
  * [scarpet](https://github.com/yahoo/tunitas-scarpet)
  * [tarwater](https://github.com/yahoo/tunitas-tarwater)
  * [temerarious-flagship](https://github.com/yahoo/temerarious-flagshiop)

The contents of the `dependencies` directory is described in more detail in the [PACKAGES](https://github.com/yahoo/tunitas-packaging/blob/master/PACKAGES.md) documentation.

## Configuration

You may acquire this repo and its dependents by running the following command:

``` bash
git clone https://github.com/yahoo/tunitas-packaging.git
git submodule init
```

The submodules will need to be configured (initialized).  If you are using a downstream repository, then you will need to reestablish the submodules to your local replia.  Instructions for doing that are beyond the scope of this introductory material, however, there is [documentation](https://git-scm.com/book/en/v2/Git-Tools-Submodules) available.

## Configuration

There is no configuration step for this repository.  The operable component in this repository is the Makefile

## Build

Once configured, the rpms can be built with the following recipe:

``` bash
cd ./rpms
make
```

The [Makefile](https://github.com/yahoo/tunitas-packaging/blob/master/rpms/Makefile) provides documentation about its use.  Also

``` bash
make usage
make list
```

## Security

The _packaging_ of the Tunitas family of technologies does not have any specific security concerns.  Each repository, individually, documents its security concerns in its respective README.md file.  Especially in case of operating an internet-facing service, such as Apanolio, Montara or Scarpet, care should be taken to operate the service in a secure mode with known best practices.  Details can be found in each of the respective respositories.

## Contribute

Please refer to [the contributing.md file](Contributing.md) for information about how to get involved. We welcome issues, questions, and pull requests. Pull Requests are welcome.

## Maintainers
- Wendell Baker <wbaker@yahooinc.com>
- The Tunitas Team at Yahoo.

You may contact us at least at <tunitas@yahooinc.com>

## License

This project is licensed under the terms of the [Apache 2.0](LICENSE-Apache-2.0) open source license. Please refer to [LICENSE](LICENSE) for the full terms.

## Origin of the Names

The Tunitas family of projects is named after geographic names (place names) of the [Tunitas](https://en.wikipedia.org/wiki/Tunitas,_California) area in San Mateo County, California.  It is a great place for mountain biking or hiking.

## The Family of Projects

In alphabetical order, an overview of the package clusters.

### Tunitas Basics

Contains common libraries and utilities.

### Apanolio

An implementation of the "North-Facing API" service for the Interactive Advertising Bureau's (IAB) [PrivacyChain](https://github.com/InteractiveAdvertisingBureau/PrivacyChain).
It is themed after [Apanolio Creek](https://en.wikipedia.org/wiki/Apanolio_Creek) in San Mateo County, California.

### Butano

An implementation of the [IAB EU Transparency &amp; Consent Framework](https://github.com/InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework).
It is themed after [Butano Creek(https://en.wikipedia.org/wiki/Butano_Creek) in San Mateo County, California.

### Grabtown

A standalone implementation of [Yahoo DataX API Specification](https://developer.yahoo.com/datax/guide/).
It is themed after [Grabtown Gulch](https://en.wikipedia.org/wiki/Grabtown_Gulch) in San Mateo County, California.
It is not yet published.

### Lobitos

An implementation of the audience management consisting of a user profile store, data subject telemetry (beacon) receivers, and some [Recency &amp; Frequency](https://en.wikipedia.org/wiki/RFM_%28customer_value%29)-type scoring algorithms.
It is themed after [Lobitos](https://en.wikipedia.org/wiki/Lobitos,_California) which is an unincorporated area within San Mateo County, California.  Lobitos was originally named Tunitas.
It is not yet published.

### Montara

An implementation of the "North-Facing" API Service for the Interactive Advertising Bureau's (IAB) [PrivacyChain](https://github.com/InteractiveAdvertisingBureau/PrivacyChain).
It is themed after [Montara Mountain](https://en.wikipedia.org/wiki/Montara,_California) in San Mateo County, California.  

### Purissima

A demonstration multi-site publisher network which uses these technologies.
It is themed after [](https://en.wikipedia.org/wiki/Purissima,_California) which is a ghost town in southwestern San Mateo County California.
It is not yet published.

### Rockaway

A reference implementation of the [DataX Service](https://developer.yahoo.com/datax/).
It is themed after [Rockaway Creek](https://en.wikipedia.org/wiki/Rockaway_Creek_%28California%29) is a small creek, in the Rockaway Beach neighborhood of Pacifica, California.
It is not yet published.

### Scarpet

A reference implementation of a resolver and identifier (document) storage service for [W3C Decentralized Identifiers](https://w3c-ccg.github.io/did-spec/).
It is themed after [Scarpet Peak](https://openthewatershed.org/the-scarper-scarpet-scarpa-peak/), which one of The Summits in San Mateo County, California.

### Tarwater

A reference implementation of the [Digi-Trust](http://www.digitru.st) universal identity system.
It is themed after [Tarwater Creek](https://en.wikipedia.org/wiki/Tarwater_Creek) in San Mateo County, California.

### Temerarious Flagship

Definition:
* [temerarious](https://en.wiktionary.org/wiki/temerarious): marked by temerity; rashness, recklessness, boldness, or presumptuousness. 
* [flagship](https://en.wiktionary.org/wiki/flagship), the most important one out of a related group. 

*mnemonic*: extending the autotools with yet more macros is … _temerarious_
*mnemonic*: the build system of any software distribution is the … _flagship_
