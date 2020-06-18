# Past Job APP

---

## Create APP

- **APP Name** : jobs

## Model

- **Class Name**: Person

- **Fields**

  | name         | CharField     |
  | ------------ | ------------- |
  | **past_job** | **TextField** |

  - makemigrations로 설계도 작성
  - migrate로 DB에 설계도 반영

---

## 직업 리스트

https://bit.ly/past_job_list

## urls

- urls 분리 필수: 프로젝트 폴더, jobs 아래 urls 
- app_name, path name 설정 필수

## views 

1. `/index/`
   - index.html 렌더링
2. `/past_life/`
   - 사용자가 form으로 날린 이름을 받아 저장 
   - DB에 사용자가 입력한 이름이 있는지 확인 
   - 만약 사용자가 입력한 이름이 DB에 있다면 기존 그 사용자의 past_job을 past_job 변수에 담기
   - 직업군 리스트에서 무작위 하나를 뽑아 사용자에게 받은 이름과 새로 뽑은 직업을 DB에 저장 
   - context로 담아서 past_life.html 로 넘김

## templates

1. 템플릿은 기본 `app/templates/app` 형태로 구분 
   - base.html: 기존의 프로젝트 폴더의 base.html 활용(템플릿 확장)  
   - index.html: 사용자에게 자신의 이름을 입력할 수 있는 form 제공 
   - past_life.html: 무작위로 선정된 직업과 사용자에게 받은 이름 출력 
   - 예시. {{ person.name }}님의 전생은 {{ person.past_job }}입니다.





### 수정 

past_life 지문 수정

사용자가 입력한 이름이 DB에 있다면 해당 이름과 직업 그대로 출력

DB에 없다면 직업 리스트에서 무작위 하나를 뽑아 DB에 이름과 직업 저장 후 출력



홈테그 부트스트렙으로 꾸미기

