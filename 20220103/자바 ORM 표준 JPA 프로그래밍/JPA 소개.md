# 1장 JPA 소개

객체와 관계형 데이터베이스 패러다임 불일치로 인한 비용이 크다.
이를 해결하기 위해 JPA를 사용한다.

> JPA는 상속, 연관관계, 객체 그래프 탐색, 비교하기와 같은 패러다임의 불일치 문제를 해결해준다.

## 1.1 SQL을 직접 다룰 때 발생하는 문제점

- 비슷한 조회/저장/수정/삭제 등의 코드에서 비슷한 일을 반복하게 된다.
  - SQL 작성하기
  - JDBC API를 사용해서 SQL 실행하기
  - 조회/저장/수정/삭제 결과를 객체로 맵핑하기
- SQL에 의존해서 개발하게 된다.
  - 어떤 새로운 column 하나를 추가했을 때, 엔티티의 속성 이외에도 해당 엔티티를 다루는 대부분의 기능(메소드)를 수정해야한다.

### 결국 이런 문제들이 있다.

1. 진정한 의미의 계층 분할이 어렵다.
2. 엔티티를 신뢰할 수 없다.
   - 새로운 column을 엔티티에 추가해도 메소드를 수정하지 않으면 해당 column이 null로 반환될 가능성이 높다.
3. SQL에 의존적인 개발을 피하기 어렵다.
   - 2번과 마찬가지의 사례들

## 1.2 패러다임의 불일치

> 관계형 데이터베이스는 데이터 중심으로 구조화되어 있고, 집합적인 사고를 요구한다. 그리고 객체지향에서 이야기하는 추상화, 상속, 다형성 같은 개념이 없다.

### 상속

> 객체는 상속이라는 긴으을 가지고 있지만 테이블은 상속이라는 기능이 없다.

- 물론, 데이터베이스 모델링에서 슈퍼타입-서브타입이라는 관계가 상속과 유사한 형태를 지니고 있긴 하다.

### 연관관계

> **객체는 참조**를 사용해서 다른 객체와 연관관계를 가지고 **참조에 접근해서 연관된 객체를 조회**한다.
> 반면에, **테이블은 외래 키**를 사용해서 다른 테이블과 연관관계를 가지고 **조인을 사용해서 연관된 테이블을 조회**한다.

- 객체를 테이블에 맞춰서 모델링하면 테이블에 저장하거나 조회할 때는 편리하다.
  - 하지만, 데이터베이스가 사용하는 방식에 맞추면 객체는 참조를 사용해 다른 객체를 조회할 수 없다.
  - 결국, 테이블에 맞춰서 모델링을 하는 방식을 지속하면 좋은 객체 모델링을 기대하기 어려워진다.
- 객체지향 모델링을 하게 되면 좋은 객체 모델링은 가능하다.
  - 다만, 이를 위해 개발자가 작성한 코드가 중간에서 객체를 테이블로 변환하는 역할을 해야 한다.

### 객체 그래프 탐색

> SQL을 직접 다루면 처음 실행하는 SQL을 따라 객체 그래프를 어디까지 탐색할 수 있는지 정해진다.

- 어디까지 객체 그래프 탐색이 가능한지 알아보려면 데이터 접근 계층인 DAO를 열어서 SQL을 직접 확인해야 한다.
- JPA는 이러한 문제를 지연로딩을 사용해 해결하고 있다.

### 비교

- 데이터베이스는 기본 키의 값으로 각 row를 구분한다.
- 객체는 동일성 비교와 동등성 비교를 이용해 객체를 비교한다.
  - 동일성<sub>identity</sub> 비교: 객체 인스턴스의 주소 값을 비교한다.
  - 동등성<sub>equality</sub> 비교: `equals()` 메소드를 사용해서 객체 내부의 값을 비교한다.

- JPA는 같은 트랜잭션일 때 같은 객체가 조회되는 것을 보장한다. 따라서 다음 코드에서 `member1`과 `member2`는 동일성 비교에 성공한다.
  ```java
  String memberId = "100";
  Member member1 = jpa.find(Member.class, memberId);
  Member member2 - jpa.find(member.class, memberId);

  member1 == member2;   // 성공한다.
  ```
- 객체 비교하기는 분산 환경이나 트랜잭션이 다른 상황까지 고려하면 더 복잡해진다.

## JPA란 무엇일까?

JPA는 자바 진영의 ORM 기술 표준이다.

- ORM: 객체와 관계형 데이터베이스를 매핑한다.

> ORM 프레임워크를 사용하면 객체를 데이터베이스에 저장할 때 `INSERT SQL`을 직접 작성하는 것이 아니라 객체를 마치 자바 컬렉션에 저장하듯이 ORM 프레임워크에 저장하면 된다.

### 왜 JPA를 사용해야 하는가?

1. 생산성
   - 자바 객체를 컬렉션에 저장하듯이 JPA에 저장할 객체를 전달하면 그 이후의 SQL 작성이나 JDBC API를 사용하는 작업을 JPA가 대신 처리해준다.
2. 유지보수
   - 필드를 추가하거나 삭제해도 수정해야할 코드가 줄어든다.
   - 따라서 유지보수해야할 코드 수가 줄어든다.
3. 패러다임의 불일치 해결
4. 성능
   - 세부적인 인터페이스로 작은 단위의 책임에서 성능 최적화에 집중할 수도 있다.
5. 데이터 접근 추상화와 벤더 독립성
   - JPA가 추상화된 데이터 접근 계층을 제공하기 때문에 특정 벤더사의 데이터베이스에 종속되지 않을 수 있다.
6. 표준
