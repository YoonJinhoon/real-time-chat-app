# real-time-chat-app
실시간 채팅 애플리케이션

# 실시간 채팅 애플리케이션

## 프로젝트 개요

이 프로젝트는 사용자 간의 실시간 채팅을 지원하는 간단한 웹 애플리케이션입니다. 아래에서 프로젝트의 기술 스택, 요구 사항, 데이터 모델 설계, API 설계, 웹 소켓 구현 계획, UI/UX 디자인 계획, 개발 일정 등을 설명합니다.

## 기술 스택

- Django: 백엔드 개발 및 데이터 관리
- Django Channels: 웹 소켓 지원
- HTML/CSS: 프론트엔드 디자인

## 요구 사항 문서

**기능 요구 사항:**

1. 사용자는 회원가입 및 로그인을 통해 애플리케이션에 접속합니다.
2. 사용자는 채팅방을 생성하거나 기존 채팅방에 참여할 수 있습니다.
3. 사용자는 채팅방에서 메시지를 입력하고 실시간으로 다른 사용자에게 전송할 수 있어야 합니다.
4. 사용자는 채팅방 목록을 볼 수 있어야 합니다.

## 데이터 모델 설계 문서

**사용자 모델:**

- 사용자 이름
- 이메일
- 비밀번호

**채팅방 모델:**

- 채팅방 이름
- 참여한 사용자 목록
- 메시지 목록

## API 설계 문서

**회원가입 API:**

- 엔드포인트: /api/signup
- 요청 형식: POST
- 응답 형식: JSON

**로그인 API:**

- 엔드포인트: /api/login
- 요청 형식: POST
- 응답 형식: JSON

**메시지 전송 API:**

- 엔드포인트: /api/send-message
- 요청 형식: POST
- 응답 형식: JSON

## 웹 소켓 구현 계획

- 웹 소켓 라이브러리: Django Channels 사용
- 웹 소켓 엔드포인트: /ws/chat/

## UI/UX 디자인 계획

- 간단한 대화형 채팅 인터페이스 설계
- 사용자 프로필 및 채팅방 목록 표시
- 실시간 메시지 갱신 및 알림 기능 추가

## 개발 일정 및 할일 목록

**단계 1: 프로젝트 초기 설정**

- 장고 기본 설정 및 프로젝트 구성
- 장고 모델 및 데이터베이스 설정
- 사용자 인증 및 권한 관리 설정

**단계 2: 실시간 채팅 구현**

- 웹 소켓 구현 및 Django Channels 설정
- 채팅방 모델과 API 구현
- 사용자 간 실시간 메시지 송수신 기능 추가
- 채팅장 목록을 표시하는 기능 추가

**단계 3: 디자인 및 UI/UX 개발**

- 채팅 애플리케이션의 UI/UX 디자인
- 사용자 프로필 및 채팅방 목록 표시
- 실시간 메시지 갱신 및 알림 기능 추가

**단계 4: 테스트, 디버깅 및 문서화**

- 테스트 케이스 작성 및 실행
- 버그 디버깅 및 수정
- 프로젝트 문서화 및 README.md 업데이트
