# Tunitas Denniston (Creek)

- Privacy-Preserving Measurement (PPM), a demonstrator with concurrency by POSIX Threads
- a test rig

This implementation uses the core data structures, algorithms & protocol machinery of the [Tunitas Keyston](https://git.tunitas.technology/repos/components/keyston/)([Yahoo](https://github.com/yahoo/tunitas-keyston)) to implement the protcol, functions and distributed operations of PPM, VDAF, HPKE.

# Scope
- Runtime simulation & test of the protocol

# Authorities (at least)

- [ppm](https://datatracker.ietf.org/wg/ppm/documents/) - <em>Privacy-Preserving Measurement</em> (PPM)
- [I-D.ietf-ppm-dap](https://ietf-wg-ppm.github.io/draft-ietf-ppm-dap/draft-ietf-ppm-dap.html) - <em>Distributed Aggregation Protocol for Privacy Preserving Measurement</em>
- [I-D.irtf-cfrg-vdaf](https://www.ietf.org/archive/id/draft-irtf-cfrg-vdaf-03.html) - <em>Verifiable Distributed Aggregation Function</em> (VDAF)
- [RFC 9180](https://www.ietf.org/rfc/rfc9180.html) - <em>Hybrid Public Key Encryption</em>

# Related Projects:

End-to-end implementations of Privacy-Preserving Measurement (PPM):
- [Tunitas Alambique (Creek)](https://git.tunitas.technology/repos/services/alambique)([Yahoo](https://github.com/yahoo/tunitas-alambique/)) - <em>a demonstrator with no concurrency</em>
- [Tunitas Denniston (Creek)](https://github.com/yahoo/tunitas-denniston)([Yahoo](https://github.com/yahoo/tunitas-denniston/)) - <em>a demonstrator with concurrency in POSIX threads</em>
- [Tunitas Honsinger (Creek)](https://github.com/yahoo/tunitas-honsinger)([Yahoo](https://github.com/yahoo/tunitas-honsinger/)) - <em>a demonstrator with multi-process concurrency coordinated by the D-Bus</em>
- [Tunitas Nuff (Creek)](https://github.com/yahoo/tunitas-nuff)([Yahoo](https://github.com/yahoo/tunitas-nuff/)) - <em>production-operability within microhttpd++</em>
- [Tunitas Woodruff (Creek)](https://github.com/yahoo/tunitas-woodruff)([Yahoo](https://github.com/yahoo/tunitas-woodruff/)) - <em>production-operability within Apache HTTPd</em>
