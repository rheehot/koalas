#
# Copyright (C) 2019 Databricks, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from databricks.koalas.version import __version__


def assert_pyspark_version():
    import logging
    pyspark_ver = None
    try:
        import pyspark
    except ImportError:
        raise ImportError('Unable to import pyspark - consider doing a pip install with [spark] '
                          'extra to install pyspark with pip')
    else:
        pyspark_ver = getattr(pyspark, '__version__')
        if pyspark_ver is None or pyspark_ver < '2.4':
            logging.warning(
                'Found pyspark version "{}" installed. pyspark>=2.4.0 is recommended.'
                .format(pyspark_ver if pyspark_ver is not None else '<unknown version>'))


assert_pyspark_version()

from databricks.koalas.namespace import *
from databricks.koalas.frame import DataFrame
from databricks.koalas.series import Series
from databricks.koalas.type import Col, pandas_wrap

__all__ = ['read_csv', 'read_parquet', 'to_datetime', 'from_pandas',
           'get_dummies', 'DataFrame', 'Series']
