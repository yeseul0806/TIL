# 깃

## 2019.07.30

### 복습
* 터미널 켜기 --> ctrl.j (안 켜지면 윈도우에서 git bash 검색하기)
* git init
* 현재 위치 파악하기 --> pwd

### git cheat sheet
* [참고 사이트](https://www.git-tower.com/blog/git-cheat-sheet/)
* [기본 명령어 모음](https://github.com/jeonghwan-kim/git-usage)

### 깃 사용
* 디렉토리 만드는 법 --> mkdir 파일명 
* 디렉토리 바꾸는 방법, 현재 위치 바꾸는 법 --> cd 파일명
* 운영체제
    * window, unix/linux : 쓰는 언어가 달라
        * 그래서 emulator를 씀
* 지금 위치하고 있는 부모 디렉토리로 가는 방법
    * 해당 디렉토리를 지정해주는 것 **(절대 경로)**
    * cd .. **(상대 경로)**
        * cd ../../../ 부모의 부모의 부모 위치로 가는 것
* cd /c/Users/umsun/Desktop/project_2/hello-dir
* cd (./)hello-dir

* ls -al
* .은 현재 디렉토리, ..은 부모 디렉토리

* 파일 지우는 법 --> rm
* 디렉토리 지우는 법 --> rm -r hello-dir , rm -rf
* 적당한 비극

### 깃 프로젝트 관리하기
* cd ./
* cd /. 의 차이
* 순서
    >* git init
    >* git status
    >* git add index.html
    >* git commit -m "파일명"
    >* git log --oneline
* 버전 만들기, 로그보기, 상태보기
* git commit -am "work 2" : add를 같이 실행하는 것, add한 이력이 있는 파일만

### 두 개 이상 파일을 만들었을 때
* 처음 만든 파일은 untracked 상태이기 때문에 add를 따로 해줘야 함
* -am은 이전에 stage에 올라간 이력이 있는 파일만 쓸 수 있음
* add : 올리고 싶지 않은 파일은 올리지 않도록 하는 안전장치이기도 함
* .ignore 파일을 만들고 깃에 안 올리고 싶은 파일을 기재한다, .ignore을 "ignore password.txt"로 add하고 커밋한다.
* git add . : 모든 하위 폴더 다 add

* ctrl c : 취소

### branch (master)
* 커밋 : 워킹카피의 스냅샷, 워킹 디렉토리를 프리징 한다
* 헤드 : 나의 워킹카피가 어느버전에서 유래한 건지를 알 수 있음, 마스터를 통해서 간접 가리킨다

#### detached 상태
>* git log --oneline --all
>* git checkout 5587e44
>* git checkout master : detached 상태에서 빠져나온 후 작업을 계속해나간다
* checkout : branch를 이동하는 것

#### reset
* reset : 마스터를 바꾼다
>* git reset 돌아가고 싶은 곳으로
>* git reset --hard 058ae65

#### branch
* 브랜치 생성
    >- git branch exp
    >- git log --oneline --all --graph
![실습 자료](./실습.jpg)
![실습 자료](./실습2.jpg)
* 브랜치 제거
    >- git branch -D exp2

#### merge
* exp에서 작업한 것을 mater와 병합하고 싶다면, master을 옮기면 됨
    1. 마스터로 체크아웃 한다
    2. 마스터로 exp를 병합한다
>* git merge exp
* git config --global core.editor "code --wait"

브랜치하고 체크아웃 같이 하는 것
* git checkout -b exp

#### conflict
각자의 사람이 똑같은 부분을 수정하고 병합했을 때 충돌이 일어난다.
코드를 비교할 때 뭉텅이씩 비교한다

merge 후 충돌했을 때 충돌한 부분 수정해주고 --> git **add** work.txt
--> 커밋

merge를 취소하고 싶을 때
* git merge --abort

![수업자료](./자료.jpg)

병합은 자주 자주 해주는 것이 좋음

>경우의 수를 많이 생각하고 고민하면 속도는 느릴지라도 더 많이 성장할 수 있다. 

## 2019.07.31
### gistory
* 가장 최신에 작업한 것이 위로 올라옴
* sample : 그냥 도움주는 파일, 신경 쓸 필요 없음
* head : 현재 나의 워킹카피가 어느버전에서 유래했는지

* ./index : 파일의 이름이 적히고
* ./object : 커밋한 내용을 확인할 수 있음
    * 같은 내용인 파일은 git에서는 하나의 파일로 관리
* 파일의 내용에 따라 파일의 이름을 만듦 : 반방향 암호화
* add를 하면 index에 해당 내용이 생성 --> commit을 하면 해당 내용의 스냅샷을 생성
* naver.html && git add naver.html && git commit -am "update naver"

### merge
* mater는 마스터로 checkout을 한다 --> master에서 exp를 땡겨온다
* exp branch를 버리고 싶을 때 --> git branch -d exp
* exp branch를 쓰고 싶을 때(master에서는 작업을 하지 않았을 때) --> 병합
* Fast-forward 병합 작업 화면
![fast_forward_병합](./fast_forward.jpg)
* merge 후 exp branch를 버리고 싶을 때 --> 헤드를 master로 옮기고 git branch -d exp --> git reset --hard B
![merge_conflict](./merge_conflic.jpg)
* mergetool을 이용하면 base까지 참조해서 수정할 수 있음 (2way로만 보이는 것을 3way로 확인할 수 있음)
* 하다가 망했다 : git merge --abort
* merge 충돌 수정한 후, git status --> add
* 명령어 다음 --help

* 파일 command line에서 만드는 법
    * vi work2.txt
    * i : 입력을 시작할 수 있음
    * ctrl c : 입력과 명령어를 바꿀 수 있음
    * 명령어 입력상태에서 :w 입력하면 저장됨, :q는 나가기

### backup
* local repository : 원래 파일
* remote repository : 백업한 파일
* Push : 로컬에서 동기화하는 명령어
* 
* ssh로 설정 (git@github.com:SeonYeong-Hwang/daitgirls.git)
* git에 있는 오픈소스 가지고 오는 법 --> git-src 폴더 형성 --> git clone git@github.com:git/git .

* 프로젝트를 처음으로 시작할 때 로컬 만들면서 원격 만들 때 : …or create a new repository on the command line
* 프로젝트를 이미 하고 있을 떄 이미 하고 있었고 나중에 원격 추가할 때 : …or push an existing repository from the command line

1. 원격으로 옮길때 쓰는 : git remote add origin git@github.com:SeonYeong-Hwang/daitgirls.git
2. 처음에 세팅 : git push --set-upstream origin master
3. ssh-keygen
4. cd /c/Users/umsun/.ssh/
5. cat id_rsa.pub

* 다른 컴퓨터에서 파일을 불러오려면? --> git clone git@github.com:SeonYeong-Hwang/daitgirls.git **.**

### 협업
* git push
* git pull
* pull = fetch + merge
* merge commit 버젼





