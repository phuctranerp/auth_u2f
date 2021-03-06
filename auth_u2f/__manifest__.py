# Copyright (C) 2017 Joren Van Onder

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301 USA

{
    'name': '2nd factor authentication via U2F',
    'author': 'Joren Van Onder',
    'depends': ['base', 'web'],
    'category': 'Extra Tools',
    'description': """Provides an additional layer of security by authenticating with a
device that supports U2F like the Yubico Yubikeys.

For documentation and source code see https://github.com/jorenvo/auth_u2f.
""",
    'license': 'LGPL-3',
    'data': [
        'views/u2f_device.xml',
        'views/u2f_templates.xml',
        'views/res_users.xml',
        'security/ir.model.access.csv',
        'security/auth_u2f_security.xml',
    ],
    'external_dependencies': {
        'python': ['u2flib_server'],
    }
}
