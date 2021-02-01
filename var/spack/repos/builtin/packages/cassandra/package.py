# Copyright 2013-2021 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Cassandra(Package):
    """
    Apache Cassandra is a highly-scalable partitioned row store. Rows are
    organized into tables with a required primary key.
    """

    homepage = "https://github.com/apache/cassandra"
    url      = "https://github.com/apache/cassandra/archive/cassandra-4.0-beta4.tar.gz"

    version('4.0-beta4', sha256='beb98898ebb9e866aa4863b952939d4b071fa4c277d826fc2589649073fa320b')
    version('4.0-beta3', sha256='860744837ebb7802a88c44d37d2a186a6753d307f0a40263ef3e15d94151c25f')
    version('3.11.10',   sha256='5a838495b9a7ec02812c42eb0c9d38519b0c0255b72109122ff84b8df642cb18', preferred=True)
    version('3.11.9',    sha256='2a6ed240a0a92e902263cea68e875e6b210b402db8d77164d2f2d95d97137cd3')

    depends_on('java', type=('build', 'run'))

    def install(self, spec, prefix):
        install_tree('.', prefix)
