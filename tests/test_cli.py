#!/usr/bin/env python3

import shlex
import shutil
import subprocess
import unittest

from src.hentai import get_logfile_path


class TestHentaiCLI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.holo_id = 308592

    def test_cli_download(self):
        command = shlex.split(f"hentai download --id {self.holo_id} --no-check")
        call = subprocess.call(command, stderr=subprocess.STDOUT)
        self.assertFalse(call, msg="Download failed for ID=%d" % self.holo_id)

    def test_cli_preview(self):
        print()
        command = shlex.split("hentai preview --id %d" % self.holo_id)
        call = subprocess.call(command, stderr=subprocess.STDOUT)
        self.assertFalse(call, msg="Preview failed for ID=%d" % self.holo_id)

    def test_cli_log(self):
        print()
        command = shlex.split("hentai log --list")
        call = subprocess.call(command, stderr=subprocess.STDOUT)
        self.assertTrue(
            get_logfile_path().exists() and (call == 0),
            msg=f"No log file was produced in '{str(get_logfile_path())}'",
        )

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(str(cls.holo_id), ignore_errors=True)
