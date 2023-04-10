#!/usr/bin/env python3

from netmiko import ConnectHandler
import unittest

def lb_onR3(ip):
    r3 = {
    "device_type": "cisco_ios",
    "ip": ip,
    "username": "pratik",
    "password": "pratik",
    "fast_cli": False
    }

    with ConnectHandler(**r3) as konnect:
            print("Successfully logged in R3")
            d = konnect.send_command("sh run int loopback99 | sec ip")
            ip1 = d.split(" ")[3]
            nm = d.split(" ")[4]
            if ip1 == '10.1.3.1' and nm == '255.255.255.0':
                print("R3s Loopback99 has IP: 10.1.3.1/24")
                return True
            else:
                print("R3s Loopback99 does not have IP: 10.1.3.1/24")
                return False

def r1_area(ip):
    r1 = {
    "device_type": "cisco_ios",
    "ip": ip,
    "username": "pratik",
    "password": "pratik",
    "fast_cli": False
    }

    with ConnectHandler(**r1) as konnect:
            print("Successfully logged in R1")
            d = konnect.send_command("sh ip protocols | inc stub")
            a = d.split(" ")[7]
            areas = a.strip(".")
            print(areas)
            if areas == '1':
                print("R1 is configured in single area")
                return True
            else:
                print("R1 is not configured in single area")
                return False

def pingr5_lb(ip):
    r5 = {
    "device_type": "cisco_ios",
    "ip": ip,
    "username": "pratik",
    "password": "pratik",
    "fast_cli": False
    }

    with ConnectHandler(**r5) as konnect:
            print("Successfully logged in R5")
            d = konnect.send_command("sh run int loopback99 | sec ip")
            lb5 = d.split(" ")[3]
            res = konnect.send_command_expect("ssh -l pratik 198.51.100.12", expect_string=r"Password:")
            res1 = konnect.send_command_timing("pratik")
            print("Logged in to R2 from R5 to ping Loopback99 on R5")
            res2 = konnect.send_command("ping "+lb5+" source loopback99")
            a1 = res2.split("\n")[4].split(" ")[3]
            if a1 != '0':
                print("Ping to R5s Loopback99 was successful from R2s Loopback99")
                return True
            else:
                print("Ping to R5s Loopback99 was unsuccessful from R2s Loopback99")
                return False

class TestClass(unittest.TestCase):

    def test_stg1(self):
        self.assertTrue(lb_onR3('198.51.100.13'))
    def test_stg2(self):
        self.assertTrue(r1_area('198.51.100.11'))
    def test_stg3(self):
        self.assertTrue(pingr5_lb('198.51.100.15'))

if __name__ == '__main__':
    unittest.main()
