##############################################################################
# Copyright (c) 2016 Daniel Farrell.  All rights reserved.
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License v1.0 which accompanies this distribution,
# and is available at http://www.eclipse.org/legal/epl-v10.html
##############################################################################

"""Tests for package build logic."""

import unittest

import vars


class TestExtractVersion(unittest.TestCase):

    """Test logic to extract ODL versions from artifact URLs."""

    nexus_url = "https://nexus.opendaylight.org/content/repositories"

    def test_boron_sr4_release_url(self):
        """Test URL of the ODL Boron SR4 release."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.release/org/opendaylight/integration/distribution-karaf/0.5.4-Boron-SR4/distribution-karaf-0.5.4-Boron-SR4.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "5")
        self.assertEqual(version["version_minor"], "4")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "1")

    def test_boron_sr4_release_zip_url(self):
        """Test URL of the ODL Boron SR4 release zip archive."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.release/org/opendaylight/integration/distribution-karaf/0.5.4-Boron-SR4/distribution-karaf-0.5.4-Boron-SR4.zip" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "5")
        self.assertEqual(version["version_minor"], "4")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "1")

    def test_carbon_release_url(self):
        """Test URL of the ODL Carbon release."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.release/org/opendaylight/integration/distribution-karaf/0.6.0-Carbon/distribution-karaf-0.6.0-Carbon.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "6")
        self.assertEqual(version["version_minor"], "0")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "1")

    def test_carbon_release_zip_url(self):
        """Test URL of the ODL Carbon release zip archive."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.release/org/opendaylight/integration/distribution-karaf/0.6.0-Carbon/distribution-karaf-0.6.0-Carbon.zip" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "6")
        self.assertEqual(version["version_minor"], "0")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "1")

    def test_carbon_sr1_release_url(self):
        """Test URL of the ODL Carbon SR1 release."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.release/org/opendaylight/integration/distribution-karaf/0.6.1-Carbon/distribution-karaf-0.6.1-Carbon.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "6")
        self.assertEqual(version["version_minor"], "1")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "1")

    def test_carbon_sr1_release_zip_url(self):
        """Test URL of the ODL Carbon SR1 release zip archive."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.release/org/opendaylight/integration/distribution-karaf/0.6.1-Carbon/distribution-karaf-0.6.1-Carbon.zip" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "6")
        self.assertEqual(version["version_minor"], "1")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "1")

    def test_boron_autorelease_url(self):
        """Test URL of an ODL Boron autorelease build."""
        # noqa ShellCheckBear
        url = "%s/autorelease-1928/org/opendaylight/integration/distribution-karaf/0.5.5-Boron-SR5/distribution-karaf-0.5.5-Boron-SR5.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "5")
        self.assertEqual(version["version_minor"], "5")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170813rel1928")

    @unittest.skip("Hangs, not sure why")
    def test_boron_autorelease_zip_url(self):
        """Test URL of an ODL Boron autorelease build zip archive."""
        # noqa ShellCheckBear
        url = "%s/autorelease-1928/org/opendaylight/integration/distribution-karaf/0.5.5-Boron-SR5/distribution-karaf-0.5.5-Boron-SR5.zip" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "5")
        self.assertEqual(version["version_minor"], "5")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170813rel1928")

    def test_carbon_autorelease_url(self):
        """Test URL of an ODL Carbon autorelease build."""
        # noqa ShellCheckBear
        url = "%s/autorelease-1940/org/opendaylight/integration/distribution-karaf/0.6.2-Carbon/distribution-karaf-0.6.2-Carbon.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "6")
        self.assertEqual(version["version_minor"], "2")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170823rel1940")

    def test_carbon_autorelease_zip_url(self):
        """Test URL of an ODL Carbon autorelease build zip archive."""
        # noqa ShellCheckBear
        url = "%s/autorelease-1940/org/opendaylight/integration/distribution-karaf/0.6.2-Carbon/distribution-karaf-0.6.2-Carbon.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "6")
        self.assertEqual(version["version_minor"], "2")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170823rel1940")

    @unittest.skip("Hangs, not sure why")
    def test_nitrogen_autorelease_url(self):
        """Test URL of an ODL Nitrogen autorelease build."""
        # noqa ShellCheckBear
        url = "%s/autorelease-1939/org/opendaylight/integration/karaf/0.7.0/karaf-0.7.0.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "7")
        self.assertEqual(version["version_minor"], "0")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170723rel1916")

    @unittest.skip("Hangs, not sure why")
    def test_nitrogen_autorelease_zip_url(self):
        """Test URL of an ODL Nitrogen autorelease build zip archive."""
        # noqa ShellCheckBear
        url = "%s/autorelease-1939/org/opendaylight/integration/karaf/0.7.0/karaf-0.7.0.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "7")
        self.assertEqual(version["version_minor"], "0")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170723rel1916")

    def test_boron_snapshot_url(self):
        """Test URL of an ODL Boron snapshot build."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.snapshot/org/opendaylight/integration/distribution-karaf/0.5.5-SNAPSHOT/distribution-karaf-0.5.5-20170813.233539-357.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "5")
        self.assertEqual(version["version_minor"], "5")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170813snap357")

    def test_boron_snapshot_zip_url(self):
        """Test URL of an ODL Boron snapshot build zip archive."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.snapshot/org/opendaylight/integration/distribution-karaf/0.5.5-SNAPSHOT/distribution-karaf-0.5.5-20170813.233539-357.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "5")
        self.assertEqual(version["version_minor"], "5")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170813snap357")

    def test_carbon_snapshot_url(self):
        """Test URL of an ODL Carbon snapshot build."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.snapshot/org/opendaylight/integration/distribution-karaf/0.6.2-SNAPSHOT/distribution-karaf-0.6.2-20170821.001151-442.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "6")
        self.assertEqual(version["version_minor"], "2")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170821snap442")

    def test_carbon_snapshot_zip_url(self):
        """Test URL of an ODL Carbon snapshot build zip archive."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.snapshot/org/opendaylight/integration/distribution-karaf/0.6.2-SNAPSHOT/distribution-karaf-0.6.2-20170821.001151-442.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "6")
        self.assertEqual(version["version_minor"], "2")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170821snap442")

    def test_nitrogen_snapshot_url(self):
        """Test URL of an ODL Nitrogen snapshot build."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.snapshot/org/opendaylight/integration/karaf/0.7.0-SNAPSHOT/karaf-0.7.0-20170815.162950-1727.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "7")
        self.assertEqual(version["version_minor"], "0")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170815snap1727")

    def test_nitrogen_snapshot_zip_url(self):
        """Test URL of an ODL Nitrogen snapshot build zip archive."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.snapshot/org/opendaylight/integration/karaf/0.7.0-SNAPSHOT/karaf-0.7.0-20170815.162950-1727.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "7")
        self.assertEqual(version["version_minor"], "0")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170815snap1727")

    def test_oxygen_snapshot_url(self):
        """Test URL of an ODL Oxygen snapshot build."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.snapshot/org/opendaylight/integration/karaf/0.8.0-SNAPSHOT/karaf-0.8.0-20170815.163312-2.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "8")
        self.assertEqual(version["version_minor"], "0")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170815snap2")

    def test_oxygen_snapshot_zip_url(self):
        """Test URL of an ODL Oxygen snapshot build zip archive."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.snapshot/org/opendaylight/integration/karaf/0.8.0-SNAPSHOT/karaf-0.8.0-20170815.163312-2.tar.gz" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "8")
        self.assertEqual(version["version_minor"], "0")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170815snap2")

    def test_carbon_multipatch_zip_url(self):
        """Test URL of an ODL Carbon multipatch-test build zip archive."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.snapshot/org/opendaylight/integration/integration/distribution/distribution-karaf/0.6.2-SNAPSHOT/distribution-karaf-0.6.2-20170822.142235-45.zip" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "6")
        self.assertEqual(version["version_minor"], "2")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170822snap45")

    def test_nitrogen_multipatch_zip_url(self):
        """Test URL of an ODL Nitrogen multipatch-test build zip archive."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.snapshot/org/opendaylight/integration/integration/distribution/karaf/0.7.0-SNAPSHOT/karaf-0.7.0-20170822.075207-274.zip" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "7")
        self.assertEqual(version["version_minor"], "0")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170822snap274")

    def test_oxygen_multipatch_zip_url(self):
        """Test URL of an ODL Oxygen multipatch-test build zip archive."""
        # noqa ShellCheckBear
        url = "%s/opendaylight.snapshot/org/opendaylight/integration/integration/distribution/karaf/0.8.0-SNAPSHOT/karaf-0.8.0-20170822.072253-6.zip" % self.nexus_url
        version = vars.extract_version(url)
        self.assertEqual(version["version_major"], "8")
        self.assertEqual(version["version_minor"], "0")
        self.assertEqual(version["version_patch"], "0")
        self.assertEqual(version["pkg_version"], "0.1.20170822snap6")