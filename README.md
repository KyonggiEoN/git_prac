# GitHub를 이용한 CI/CD workflow
​Git을 이용하는 방법은 단순히 자신이 만드는 프로그램의 버전 관리에 지나지 않습니다.

진정한 Git의 유용성은 다른 사람들과 함께 GitHub를 사용하여 협업(Collaboration)하고, 변경 사항을 자동으로 검증(CI/CD)할 때 나옵니다.

​이 리포지토리에서는 EoN 동아리 부원들이 실제 프로젝트를 진행하듯 시뮬레이션하며 Git 흐름을 익힙니다.

## ​진행 방식

​협업 상황에 따라 선택할 수 있는 두 가지 경로가 있습니다.

### ​방법 1. 오픈소스 프로젝트 참여 방식 (Fork & Pull Request)

​자신의 계정으로 저장소를 복제해와서 작업한 뒤 제안하는 방식입니다. 권한이 없는 외부 프로젝트에 기여할 때 주로 사용합니다.

- ​Fork: GitHub 우측 상단의 Fork 버튼을 눌러 git_prac 리포지토리를 자신의 계정으로 가져옵니다.

- ​Clone: 자신의 리포지토리 주소를 복사해 터미널에서 로컬로 복제합니다.
git clone https://github.com/{본인_계정}/git_prac.git

- ​Upstream 등록: 원본 저장소의 업데이트를 받기 위해 원본을 upstream이라는 이름으로 등록합니다.
git remote add upstream https://github.com/Kyonggi-eon/git_prac

- ​Issue 확인: GitHub Issues 탭에서 해결할 문제를 확인하고, 댓글로 "제가 작업하겠습니다!"라고 알립니다.
​Branch 생성: 새로운 작업을 위해 브랜치를 만듭니다. (규칙: fix/이슈번호-이름)
git switch -c fix/issue-1-idamin

- ​Code Fix: LLM이나 구글링 등을 활용해 문제를 수정합니다.

- ​Test: 수정 후 프로그램을 실행하여 정상 동작을 반드시 확인합니다. (이것이 로컬 유닛 테스트의 시작입니다.)
​Commit: 변경 사항을 저장합니다.
git add .
git commit -m "fix: issue-1 해결 및 테스트 완료"

- ​Sync Upstream: 작업 중 원본에 추가된 내용이 있을 수 있으므로 최신 코드를 불러옵니다.
git pull upstream main (충돌 발생 시 팀원과 상의하여 해결)

- ​Push: 자신의 GitHub(origin)로 수정본을 올립니다.
git push origin fix/issue-1-idamin

- ​Pull Request (PR): GitHub 웹사이트에서 원본 저장소(Kyonggi-eon/git_prac)로 PR을 보냅니다.
​Code Review: 모든 PR은 최소 2명 이상의 Approve를 받아야 Merge(합치기) 되도록 설정되어 있습니다. 리뷰어의 의견을 반영해 코드를 수정해보세요.

### ​방법 2. 협업자 등록 방식 (Shared Repository Workflow)

​저장소의 쓰기 권한을 직접 부여받아 작업하는 방식입니다. 팀 프로젝트에서 가장 많이 쓰입니다.

​주의: 이 방식을 사용하려면 22기 회장에게 GitHub 닉네임을 보내 'Collaborator' 초대를 먼저 받아야 합니다.

- ​Clone: 터미널에 원본 저장소를 바로 클론합니다.
git clone https://github.com/kyonggi-eon/git_prac
​Re-open: VS Code에서 해당 폴더를 다시 열어 루트 경로가 프로젝트 폴더가 되도록 합니다.

- ​Issue Claim: 해결하고 싶은 Issue에 댓글을 달아 작업 우선권을 확보합니다.

- ​Branch Switch: 반드시 새 브랜치에서 작업을 시작합니다. (main 브랜치에 직접 푸시 금지)
git switch -c fix/issue-2-damin

- ​Fix & Verify: 코드를 수정하고 로컬에서 정상 작동하는지 확인합니다.

- ​Stage & Commit: 변경된 파일을 올리고 기록을 남깁니다.
git status (상태 확인)
git add .
git commit -m "fix: issue-2 버그 수정"

- ​Push: 자신이 작업한 브랜치만 서버에 올립니다.
git push origin fix/issue-2-damin
​PR & CI 확인: PR을 올리면 GitHub Actions가 자동으로 빌드와 테스트를 수행합니다. 초록색 체크 표시(All checks have passed)가 뜨는지 확인하세요!

## ​💡 유의사항 및 팁

- ​Commit Message: 가급적 fix: , feat: , docs:  같은 접두사를 붙여 어떤 성격의 작업인지 명시해주세요.
- ​Conflict(충돌): 같은 줄을 여러 명이 수정하면 발생합니다. 당황하지 말고 VS Code의 충돌 해결 도구를 사용해 '수용할 변경 사항'을 선택하세요.
- ​Branch 관리: 작업이 끝난(Merge된) 브랜치는 git branch -d 브랜치명으로 삭제하여 로컬을 깔끔하게 유지하는 것이 좋습니다.