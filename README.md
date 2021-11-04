# DataPipeline-PUBG
pubg에서 제공하는 유저 데이터 및 인게임 데이터의 파이프라인을 구축하는 프로젝트  
제작기간: 2021.08.~2021.09

## 프로젝트 기획 배경
게임을 좋아하고 게임 데이터를 이용해 무엇을 해볼 수 있을까 고민하던 와중  
즐겨하는 배틀그라운드 데이터를 이용한 다양한 프로젝트(인게임 데이터 분석 및 플레이 피드백)를 차후에 진행할 목적으로  
데이터 파이프라인을 구축하는 프로젝트를 기획함.  

## 만들고자 하는 솔루션  
데이터 베이스에 접근해 sql문을 사용해 인게임 데이터를 조회 할 수 있는 DB구축과 AWS상에서 DB운용  

## 프로젝트 진행 과정  
PUBG Developer Portal에서는 API를 통해 다양한 데이터를 json파일로 제공 중(플레이어, 매치 데이터등).
API키를 발급받아 제공된 데이터 사용.
프로젝트 진행 당시 최근 10게임 데이터(유저, 킬, 데미지, 소생 등등)를 사용하여 csv 파일과(로컬, json to dataframe으로 변환작업) 
MYSQL DB 구축(AWS DB 인스턴스 사용)

## 사용 언어
- Python: API request, json file변환, 필요한 data추출 후 dataframe화 진행 
- SQL : 데이터 구축 및 조회(MySQL, MySQLWorkbench 사용)

## 사용한 스택
<p align="left"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> <a href="https://aws.amazon.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" alt="aws" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank"> </a> </p>
