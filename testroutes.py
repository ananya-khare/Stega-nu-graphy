import os
import tempfile

import pytest

import requests

def test_encode():
    resp = requests.get('http://65.0.127.149:8081/')
    assert resp.status_code == 200
    assert resp.url == 'http://65.0.127.149:8081/'

def test_decode():
    resp = requests.get('http://65.0.127.149:8081/decode')
    assert resp.status_code == 200

def test_info():
    resp = requests.get('http://65.0.127.149:8081/info')
    assert resp.status_code == 200

def test_invalid():
    resp = requests.get('http://65.0.127.149:8081/invalid')
    assert resp.status_code == 404