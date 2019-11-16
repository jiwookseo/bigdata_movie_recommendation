# Honey Bee <small>빅데이터 기반 영화 추천 서비스</small>

### Service

- Movie Lens 1,000,000 데이터를 이용한 KNN algorithm, collaboration filtering 을 통한 개인화 영화 추천 서비스
- Netflix 를 Cloning 한 클라이언트 디자인

#### Architecture

- 방대한 데이터를 작은 단위로 Pagenation 하여 호출
- JWT 방식을 사용한 토큰 기반 인증 시스템
- RESTful API 서버 구현
- Webpack 을 통한 클라이언트 구현

&nbsp;

### Use our service. [Honey Bee](http://52.78.81.59/)

![main](assets/main.png)

&nbsp;

## 1. Detail Feature

#### 1) 연령대, 직군, 성별별 영화 추천

- 군집별 사용자들이 선호하는 추천 영화 목록을 제공합니다.

![group recm](assets/movie_list.png)

&nbsp;

#### 2) 구체적인 영화 정보와 비슷한 영화 추천

- 영화의 줄거리와 장르, 평균 평점 등 정보 제공

  ![movie detail](assets/movie_detail.png)

* KNN algorithm 을 통한 유사 영화를 비슷한 작품으로 제공합니다.

  ![similar movies](assets/similar_list.png)

&nbsp;

## 2. Built With

#### Deploy

Deploying separated Server & Client & DB

- AWS EC2
- Nginx
- uWSGI

&nbsp;

#### Frontend

SPA with Vue CLI

- Vue CLI
- Vuex
- Sass

&nbsp;

#### Backend

REST API with Django REST framework

- Django
- Django REST framework
- Django REST framework-jwt
- SQLite3

&nbsp;

## 3. Deployed Service or Local Install

#### 1) Deployed Service

[AWS](https://aws.amazon.com/) 을 이용해 배포했습니다.

- [Go to Honey Bee](http://52.78.81.59/)

#### 2) Local Installation and Run Server

1. Installation

   - Git Clone

     ```bash
      git clone https://github.com/jiwookseo/bigdata_movie_recommendation.git
     ```

   - or [Download ZIP](https://github.com/jiwookseo/bigdata_movie_recommendation/archive/develop.zip)

   &nbsp;

2. Settings

   coming soon...

&nbsp;

## 4. Authors

- Frontend part [Dowoo Kim](https://github.com/dowookims)
- API & Deploy part [Jiwook Seo](https://github.com/jiwookseo)
- JWT Authentication part [Jisun Lee](https://github.com/jisun1002)
- JWT Authentication & admin part [Wonjin Lee](https://github.com/Terpe66)
- Algorithm & admin part [Sungjik Cho](https://github.com/sungjik6875)
