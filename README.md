# Aftercare-Kisses

Sakurya & Himawari

---

## **Git** 提交规范

尽量一次只提交一个功能，格式为:

```text
[类型][作用域][标题]
[正文]
```

示例:

```text
feat(Pkg-ConfigEditor): 添加配置编辑器内核组件
该包用于统一加载与编辑 json / toml / database 等配置源，核心能力包括：

- 支持对 JSON、TOML 格式数据进行读取与增删改查
- 将多种配置格式统一解析为 Python dict 对象
- 自动构建“类型格式树”，解析每个字段的键名、值、与其对应的类型
  - 示例：{"name": "lian", "age": 19} ➜ {"name: str": "lian: str", "age: str": "19: int"}
- 为后续类型分析、TypedDict 生成、配置校验等提供底层支持
```

### 类型及说明

| 类型     | 说明                     |     | 类型       | 说明              |
| -------- | ------------------------ | --- | ---------- | ----------------- |
| `feat`   | 新功能                   |     | `refactor` | 重构代码          |
| `fix`    | 修 bug                   |     | `docs`     | 修改文档 (README) |
| `style`  | 改代码风格               |     | `test`     | 加测试文件        |
| `chore`  | 改杂项 (.gitignore, .sh) |     | `perf`     | 性能优化          |
| `ci`     | CI/CD 相关改动           |     | `build`    | 改构建或依赖      |
| `rerert` | 回滚提交                 |

---
