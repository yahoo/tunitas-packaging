# Tunitas Keyston (Creek)

- Privacy-Preserving Measurement (PPM)
- Verifiable Distributed Aggregation Function (VDAF)
- Hypbrid Public Key Encryption (HPKE)

These are the core data structures, algorithms & protocol machinery of the Tunitas rendering of PPM, VDAF & HPKE.

# Scope

- Protocol Data Structures
- Wireline Packet Management

# Alternatives

To show that the PPM system "works" end-to-end, there are demonstrators at various levels of granularity:

0. single process no concurrency -> a simulation using in-memory events in [Tunitas Alambique (Creek)](https://git.tunitas.technology/repos/service/alambique/)([Yahoo](https://github.com/yahoo/tunitas-alambique/)).
   runs on the same host (obviously) with thread-based concurrency (easy debugging)
0. single process with concurrency -> a simulation using pthreads in [Tunitas Denniston (Creek)](https://git.tunitas.technology/repos/service/denniston/)([Yahoo](https://github.com/yahoo/tunitas-denniston/)).
   runs on the same host (obviously) with thread-based concurrency (easy debugging)
1. multiple process with concurrency -> a simulation using D-Bus in [Tunitas Honsinger](https://https://git.tunitas.technology/repos/service/honsinger/)([Yahoo](github.com/yahoo/tunitas-honsinger)).
   runs on the same host using the session-level D-Bus for inter-process communication.
2. multiple hosts -> using microhttpd++ in [Tunitas Nuff](https://https://git.tunitas.technology/repos/service/nuff/)([Yahoo](github.com/tunitas-nuff)).
   supports multiple hosts, with wireline packets, with full-dress encryption
3.  multiple hosts -> using Apache HTTPd in [Tunitas Woodruff](https://https://git.tunitas.technology/repos/service/woodruff/)([Yahoo](github.com/tunitas-woodruff)).
   supports multiple hosts, with wireline packets, with full-dress encryption

# Authorities (at least)

- [ppm](https://datatracker.ietf.org/wg/ppm/documents/) - <em>Privacy-Preserving Measurement</em> (PPM)
- [I-D.ietf-ppm-dap](https://ietf-wg-ppm.github.io/draft-ietf-ppm-dap/draft-ietf-ppm-dap.html) - <em>Distributed Aggregation Protocol for Privacy Preserving Measurement</em>
- [I-D.irtf-cfrg-vdaf](https://www.ietf.org/archive/id/draft-irtf-cfrg-vdaf-03.html) Verifiable Distributed Aggregation Function (VDAF)
- [RFC 9180](https://www.ietf.org/rfc/rfc9180.html) - <em>Hybrid Public Key Encryption</em>

# Related projects:

End-to-end implementations of Privacy-Preserving Measurement (PPM):
- [Tunitas Alambique (Creek)](https://git.tunitas.technology/repos/services/alambique)([Yahoo](https://github.com/yahoo/tunitas-alambique/)) - <em>a demonstrator with no concurrency</em>
- [Tunitas Denniston (Creek)](https://github.com/yahoo/tunitas-denniston)([Yahoo](https://github.com/yahoo/tunitas-denniston/)) - <em>a demonstrator with concurrency in POSIX threads</em>
- [Tunitas Honsinger (Creek)](https://github.com/yahoo/tunitas-honsinger)([Yahoo](https://github.com/yahoo/tunitas-honsinger/)) - <em>a demonstrator with multi-process concurrency coordinated by the D-Bus</em>
- [Tunitas Nuff (Creek)](https://github.com/yahoo/tunitas-nuff)([Yahoo](https://github.com/yahoo/tunitas-nuff/)) - <em>production-operability within microhttpd++</em>
- [Tunitas Woodruff (Creek)](https://github.com/yahoo/tunitas-woodruff)([Yahoo](https://github.com/yahoo/tunitas-woodruff/)) - <em>production-operability within Apache HTTPd</em>
