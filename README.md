# KakaoTalk chatting Analyzer

카카오톡 채팅 로그를 분석해줍니다.

  - 채팅방 유저
  
  - 주요 채팅 시간
  
  - 형태소 분석
  
  - Word Cloud 생성

### Word Cloud 란?
> A tag cloud (word cloud or wordle or weighted list in visual design) is a novelty visual representation of text data, typically used to depict keyword metadata (tags) on websites, or to visualize free form text. Tags are usually single words, and the importance of each tag is shown with font size or color.[2] This format is useful for quickly perceiving the most prominent terms to determine its relative prominence. When used as website navigation aids, the terms are hyperlinked to items associated with the tag. [WIKIPEDIA](https://en.wikipedia.org/wiki/Tag_cloud)
>
> 테스트 환경 : PC KakaoTalk

## 제공하는 기능
- 채팅방 유저
  - 현재 채팅방 기준으로 모든 유저 목록을 보여줍니다.
  
  ```python
  print(x for x in all_userlist())
  ```
  
  ```
  - All user name (3) # Number of Users
  user A
  user B
  user C
  ```
  
- 주요 채팅 시간
  - 오전 / 오후를 나눠서 백분율로 통계 내줍니다.
  
  ```python
  pi_names = ['AM', 'PM']
  plt.pie(chat_time(date.count('오전'), date.count('오후')), labels=pi_names, autopct='%1.2f%%')
  plt.title("Categorized by Chat Time")
  plt.show()
  ```
    
  <p align=center>
    <img src="https://github.com/Xenia101/KakaoTalk-chatting-Analyzer/blob/master/img/pie%20graph.PNG?raw=true">
  </p>

- 형태소 분석
  - 형태소 분석 후 가장 많이 쓰이는 명사 Top 10 을 보여줍니다.
  
  ```python
  count_list = Counter(noun_adj)
  for x in count_list.most_common(10):
    print(x)
  ```
  
  ```
  - Most Common Noun,adj (word, counts)
  ('example', 2023)
  ('of', 1876)
  ('word', 1136)
  ...
  ```

- Word Cloud 생성
  - Text 분석 후 Word Cloud 를 생성해줍니다.
  
  - 예시 이미지
  
  <p align=center>
    <img src="https://github.com/Xenia101/KakaoTalk-chatting-Analyzer/blob/master/img/wikiTag_cloud.png?raw=true">
  </p>
  
## 실행 환경
- Windows 10 or Ubuntu Linux
- Python 3.x

## 사용 방법

### GET KakaoTalk Chatting Log (PC)

1. 분석을 원하는 대화방에서 <strong>[메뉴]</strong> 선택

2. <strong>[대화내용]</strong> -> <strong>[내보내기]</strong> 선택 후 input 폴더에 저장

3. input 폴더에 저장된 .txt 파일 활용
    ```python
    filename = './input/KakaoTalk_20191228_2200_19_145_group.txt'
    ```

