"""
=========================================================
AI Helpdesk Assistant
Helpdesk Knowledge Base

This file stores business knowledge for each ticket
category predicted by the Machine Learning model.

Author: Thangaraj
=========================================================
"""

HELPDESK_DATA = {

    "Password Reset": {

        "assigned_team": "IT Service Desk",

        "priority": "Medium",

        "eta": "15 - 30 Minutes",

        "resolution": [

            "Verify that Caps Lock is turned off.",

            "Ensure you are entering the correct username and password.",

            "If you recently changed your password, try the new password.",

            "If your account is locked, contact the IT Service Desk.",

            "Provide the exact error message if the issue continues."

        ]

    },

    "VPN Issue": {

        "assigned_team": "Network Support",

        "priority": "High",

        "eta": "30 Minutes",

        "resolution": [

            "Check your internet connection.",

            "Restart the VPN application.",

            "Verify your VPN username and password.",

            "Reconnect to the VPN.",

            "If the problem continues, contact Network Support."

        ]

    },

    "Email Issue": {

        "assigned_team": "Messaging Team",

        "priority": "Medium",

        "eta": "30 - 60 Minutes",

        "resolution": [

            "Check your internet connection.",

            "Restart your email application.",

            "Verify your email credentials.",

            "Check if your mailbox storage is full.",

            "Contact the Messaging Team if the issue persists."

        ]

    },

    "Hardware Issue": {

        "assigned_team": "Desktop Support",

        "priority": "High",

        "eta": "2 - 4 Hours",

        "resolution": [

            "Restart the computer.",

            "Check all hardware connections.",

            "Disconnect recently connected devices if applicable.",

            "Note any error messages displayed.",

            "Contact Desktop Support for further diagnosis."

        ]

    },

    "Printer Issue": {

        "assigned_team": "Desktop Support",

        "priority": "Low",

        "eta": "1 Hour",

        "resolution": [

            "Ensure the printer is powered on.",

            "Check paper and toner levels.",

            "Verify the printer is connected to the network.",

            "Clear any stuck print jobs.",

            "Contact Desktop Support if the issue continues."

        ]

    },

    "Network Issue": {

        "assigned_team": "Network Support",

        "priority": "High",

        "eta": "30 Minutes",

        "resolution": [

            "Restart your router or network connection if applicable.",

            "Check whether other websites are accessible.",

            "Reconnect to the Wi-Fi network.",

            "Verify that network cables are properly connected.",

            "Contact Network Support if connectivity is still unavailable."

        ]

    },

    "Software Installation": {

        "assigned_team": "Software Support",

        "priority": "Low",

        "eta": "1 Business Day",

        "resolution": [

            "Verify that the software is approved by your organization.",

            "Ensure your computer has enough storage.",

            "Close unnecessary applications before installation.",

            "Restart the computer after installation if required.",

            "Contact Software Support if installation fails."

        ]

    },

    "Account Access": {

        "assigned_team": "Identity & Access Management",

        "priority": "Medium",

        "eta": "1 Hour",

        "resolution": [

            "Verify your username.",

            "Ensure your password is correct.",

            "Check whether your account is locked.",

            "Confirm you have permission to access the application.",

            "Contact the Identity & Access Management team if access is still denied."

        ]

    },

    "Security/Phishing": {

        "assigned_team": "Information Security",

        "priority": "Critical",

        "eta": "Immediate",

        "resolution": [

            "Do not click suspicious links.",

            "Do not download unknown attachments.",

            "Report suspicious emails immediately.",

            "Change your password if you suspect compromise.",

            "Contact the Information Security team immediately."

        ]

    },

    "Access Request": {

        "assigned_team": "Identity & Access Management",

        "priority": "Low",

        "eta": "1 - 2 Business Days",

        "resolution": [

            "Provide the name of the application or system you need access to.",

            "Obtain manager approval if required by your organization.",

            "Wait for access confirmation from the IT team.",

            "Verify access after it has been granted.",

            "Contact the Identity & Access Management team if access is delayed."

        ]

    }

}