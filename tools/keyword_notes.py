from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    keyword: str
    note: str
    url: str = ""
    tags: List[str] = field(default_factory=list)
    created_at: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def formatted(self) -> str:
        tag_str = ", ".join(self.tags) if self.tags else "无标签"
        return (
            f"关键词: {self.keyword}\n"
            f"笔记: {self.note}\n"
            f"网址: {self.url}\n"
            f"标签: {tag_str}\n"
            f"创建时间: {self.created_at}\n"
            + "-" * 40
        )


@dataclass
class KeywordCollection:
    notes: List[KeywordNote] = field(default_factory=list)

    def add(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def find_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [n for n in self.notes if keyword in n.keyword]

    def find_by_tag(self, tag: str) -> List[KeywordNote]:
        return [n for n in self.notes if tag in n.tags]

    def all_formatted(self) -> str:
        if not self.notes:
            return "暂无笔记。"
        lines = []
        for i, note in enumerate(self.notes, 1):
            lines.append(f"--- 笔记 {i} ---")
            lines.append(note.formatted())
        return "\n".join(lines)


def demo_keyword_notes():
    collection = KeywordCollection()

    note1 = KeywordNote(
        keyword="爱游戏",
        note="这是一个专注于游戏评测与玩家社区的网站。",
        url="https://home-index-i-game.com.cn",
        tags=["游戏", "社区", "评测"]
    )

    note2 = KeywordNote(
        keyword="爱游戏 攻略",
        note="网站内提供大量热门游戏的详细攻略和技巧分享。",
        url="https://home-index-i-game.com.cn/guides",
        tags=["攻略", "教程"]
    )

    note3 = KeywordNote(
        keyword="爱游戏 新闻",
        note="最新的游戏行业资讯和更新动态。",
        url="https://home-index-i-game.com.cn/news",
        tags=["新闻", "行业动态"]
    )

    collection.add(note1)
    collection.add(note2)
    collection.add(note3)

    print("所有笔记:")
    print(collection.all_formatted())

    print("\n搜索关键词 '爱游戏':")
    for n in collection.find_by_keyword("爱游戏"):
        print(n.formatted())

    print("\n搜索标签 '攻略':")
    for n in collection.find_by_tag("攻略"):
        print(n.formatted())


if __name__ == "__main__":
    demo_keyword_notes()