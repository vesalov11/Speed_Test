import speedtest #pip install speedtest-cli
test = speedtest.Speedtest()
download = test.download()
uplload = test.upload()
print(f"Download speed:{download}")
print(f"Upload speed:{uplload}")