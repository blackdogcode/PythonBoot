# Chapter01-02
# 파이썬 중급
# 개발 가상 환경 설정 테스트 코드

import pendulum
from datetime import datetime

pst = pendulum.timezone('America/Los_Angeles')
ist = pendulum.timezone('Asia/Seoul')

# 타입 확인
print(type(pst))

# 타임존 시간 출력
print('Current Date Time in PST =', datetime.now(pst))
print('Current Date Time in IST =', datetime.now(ist))

# 타입 확인
print(type(ist))
