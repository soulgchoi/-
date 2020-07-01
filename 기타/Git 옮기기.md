# Git 옮기기

gitlab 에서 github 으로 **커밋로그 그대로** 옮기기

### 저장소 옮기기

1. 원본 저장소를 복사한다.

```bash
$ git clone --mirror [원본 저장소 경로] <또는 이름>
```

2. 클론한 디렉토리 안으로 이동

```bash
$ cd [원본 저장소 이름].git
```

클론할 때 이름을 설정했으면 이름으로

3-1. 이동할 원격 저장소 경로 지정

```bash
$ git remote set-url --push origin [이동할 원격 저장소]
```

이렇게 했을 경우,

새 원격 저장소로 push

```bash
$ git push --mirror
```

3-2. 바로 원격 저장소에 push

```bash
$ git push --mirror [이동할 원격 저장소]
```

### 특정 커밋 이력을 삭제하고 싶을 때

1. bfg-repo-cleaner 를 다운받는다. (jdk 도 깔려있어야 함)

위에서 클론한 디렉토리까지 이동했을 때 다음부터 수행

2-1. 100M 이상 커밋 이력 삭제

```bash
$ java -jar ~/bfg-x.x.x.jar --strip-blobs-bigger-than 100M
```

경로와 버전은 달라질 수 있다.

2-2. 특정 폴더나 파일을 삭제하고 싶을 때

```bash
$ java -jar ~/bfg-x.x.x.jar --delete-folder "[삭제할 폴더명]"
$ java -jar ~/bfg-x.x.x.jar --delete-files "{[파일명], [파일명]}"
```

여러 개를 삭제할 수 있다.

2-3. `protected` 커밋이라 삭제가 안될 때

```bash
$ java -jar ~/bfg-x.x.x.jar --no-blob-protection [하고싶은 것]
```

프로텍션을 무시해버린다.

3. 원격 저장소로 push