# EoN 스마트 동아리 관리 시스템 - 20 Bugs Edition (버그 헌트)

이 프로젝트는 이제 **"버그 수정 훈련소"**로 변경되었습니다.
프로그램 곳곳에 심어진 20개의 치명적인 오류를 찾아 고치는 것이 목표입니다.

## 📂 프로젝트 폴더 구조

```
root/
├── main.py                # [진입점] 실행하자마자 버그가 터질 것입니다.
├── test.ipynb             # [테스트] 통합 테스트를 위한 노트북
├── src/                   # [버그] 오류가 가득한 코드들
│   ├── calculator.py      # 계산기 (문법, 논리 오류)
│   ├── attendance.py      # 출석부 (Index, Key, Type 오류)
│   ├── string_utils.py    # 문자열 처리 (무한 루프 등)
│   └── game.py            # 미니게임 (스코프, Assert 오류)
├── data/
│   └── member_list.json   # Conflict 연습을 위해서 준비된 파일
└── docs/
    └── system_structure_ko.md # 시스템 구조 설명 및 과제 설명
```

## 🎯 미션: 20개의 버그를 잡아라!

여러분은 `FIXME` 주석이 달린 코드를 찾아 수정해야 합니다. 
각자 하나의 버그를 맡아 해결하고 PR을 보내세요.

### 버그 목록 (예고)
1. **SyntaxError**: 콜론(`:`)이 없거나 들여쓰기가 엉망인 코드.
2. **RuntimeError**: 0으로 나누기, 존재하지 않는 변수 사용.
3. **LogicError**: 더하기 함수가 빼기를 하는 등.
4. **Infinite Loop**: 프로그램이 멈추지 않는 무한 루프.

### 협업 규칙
1. **Issue 확인**: 자신이 어떤 버그를 고칠지 동료들과 상의하세요.
2. **코드 수정**: `main.py`에 있는 통합 테스트나, 각 파일의 로직을 고치세요.
3. **PR 제출**: "Fix: calculator.py 0으로 나누기 오류 해결" 등의 제목으로 PR을 보내세요.

## Conflict 연습하기

각자 수정을 하면서 data/member_list.json 파일을 수정하세요.

```json
{
    "members": [
        {
            "name": "Club President",
            "role": "Admin",
            "bio": "Managing the club."
        }
    ]
}
```

이 구조를 유지하면서, 자신의 이름과 역할을 임의로 추가하면 됩니다. (닉네임도 됩니다)

예를 들어, Mark를 추가한다면

```json
{
    "members": [
        {
            "name": "Club President",
            "role": "Admin",
            "bio": "Managing the club."
        },
        {
            "name": "Mark",
            "role": "Member",
            "bio": "Mark is a member of the club."
        }
    ]
}
```

대부분은 이름을 추가하고, push하는 과정에서 conflict가 발생할 것입니다.