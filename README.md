# Raspberry Pi Super Clock

该项目将您的Raspberry Pi变成一个功能丰富的超级时钟。它包括：

- 当前时间显示
- 天气更新
- 闹钟功能

## 要求

- Raspberry Pi（任何具有互联网连接的型号）
- 安装了Raspberry Pi OS的MicroSD卡
- 互联网连接
- Python 3

## 安装

1. **设置Raspberry Pi:**
   - 在microSD卡上安装Raspberry Pi OS并设置Raspberry Pi。
   - 确保您的Raspberry Pi已连接到互联网。

2. **克隆仓库:**
   ```bash
   git clone https://github.com/yourusername/raspberry-pi-super-clock.git
   cd raspberry-pi-super-clock
   ```

3. **安装依赖项:**
   ```bash
   sudo apt update
   sudo apt install python3-pip
   pip3 install -r requirements.txt
   ```

4. **配置环境变量:**
   - 将您的API密钥添加到环境变量中。例如，您可以在`~/.bashrc`或`~/.bash_profile`中添加以下行：
     ```bash
     export WEATHER_API_KEY="YOUR_OPENWEATHERMAP_API_KEY"
     ```
   - 然后重新加载您的shell配置：
     ```bash
     source ~/.bashrc  # 或者 source ~/.bash_profile
     ```

5. **配置文件:**
   - 将`config.example.json`重命名为`config.json`，并填写您的详细信息（例如城市名称）。
   - 将`alarms.example.json`重命名为`alarms.json`，并填写您的闹钟时间。

## 使用

运行主脚本以启动超级时钟:
```bash
python3 super_clock.py
```

## 功能

- **当前时间显示:**
  以24小时格式显示当前时间。

- **天气更新:**
  使用API获取并显示当前天气信息。

- **闹钟:**
  允许您通过配置文件设置闹钟。

## 配置

`config.json`文件包含超级时钟的城市配置。
`alarms.json`文件包含闹钟设置。

## 许可证

此项目是根据MIT许可证许可的。有关详细信息，请参阅`LICENSE`文件。

## 贡献

欢迎贡献！请提交问题或提交拉取请求。