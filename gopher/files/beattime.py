#!/usr/pkg/bin/python

from datetime import datetime, timedelta
BMT = datetime.utcnow() + timedelta(hours=1)
beats = (BMT.second + (BMT.minute * 60) + (BMT.hour * 3600)) / 86.4
print('@'+'%07.3f'%beats)
