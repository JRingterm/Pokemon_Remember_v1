# DRF로 구현한 Pokemon_Remember_v1 API
## 해당 프로젝트는 React로 작성한 Pokemon_Remember_UI_v1과 연동하는 백엔드이다.

## 용도
포켓몬 배틀을 즐기는 사람이라면, 만든 실전개체 포켓몬이 너무 많다던가, 한 종류의 포켓몬이라도 다양한 역할을 수행하기 때문에, 어떤 목적으로 개체를 만들었는지 까먹을 때가 있다.

내가 만든 실전개체 포켓몬이 어떠한 조정을 했고, 어떠한 역할을 수행하는지 기록, 삭제, 수정, 조회할 수 있도록 만든 API이다.

## 모델설명

### id
고유값. api 데이터를 구분할 때 쓰인다.

### name
포켓몬의 이름. 웬만하면 포켓몬 고유이름 그대로 입력하도록 하자. (검색때 편리)

### nature
포켓몬의 성격

### ability
포켓몬의 특성

### teratype
포켓몬의 테라스탈 타입

### stats
포켓몬의 노력치

### skills
포켓몬의 기술배치

### item
포켓몬의 지닌도구

### description
포켓몬의 조정의미, 역할


# SECRET_KEY를 그대로 푸쉬해버린 실수

### settings.py에 있는 SECRET_KEY는 보안과 관련된 민감한 파일. 나의 실수로 여태껏 해왔던 모든 커밋에 SECRET_KEY가 노출되었다.

git filter-branch --tree-filter 'rm Pokemon_Remember_v1/settings.py' HEAD
git push origin master --force

위 명령어로, 모든 커밋 히스토리에서 settings.py 파일을 삭제했고, SECRET_KEY를 분리한 가장 최근 커밋에만 settings.py가 존재한다.

앞으로는 프로젝트를 시작하자마자 SECRET_KEY를 분리해서 이와같은 일이 다시는 발생하지 않도록 유의할 것!