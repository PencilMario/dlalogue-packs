init python:
    # -*- coding: utf-8 -*-
    from ftplib import FTP
    import time,tarfile,os,sys,datetime
    import zipfile
    appdata = os.getenv("APPDATA")
    m_name = persistent._mas_monika_nickname
    p_name = persistent.playername
    
    persistent.CloudBackupLastTime = [None, None]

    #连接ftp
    def ftpconnect(host,port, username, password):
        ftp = FTP()
        # 打开调试级别2，显示详细信息
        # ftp.set_debuglevel(2)
        ftp.connect(host, port)
        ftp.login(username, password)
        return ftp
    
    #从ftp下载文件
    def downloadfile(ftp, remotepath, localpath):
        # 设置的缓冲区大小
        bufsize = 1024
        fp = open(localpath, 'wb')
        ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
        ftp.set_debuglevel(0)# 参数为0，关闭调试模式
        fp.close()
    
    #从本地上传文件到ftp
    def uploadfile(ftp, remotepath, localpath):
        bufsize = 1024
        fp = open(localpath, 'rb')
        ftp.storbinary('STOR ' + remotepath, fp, bufsize)
        ftp.set_debuglevel(0)
        fp.close()
    
    def uploadSave():
        ftp = ftpconnect("mas.backup.0721play.icu", 21, "mas_backup_0721play_icu", "3RNNNwYYetBi3LHw")
        if not renpy.android:
            dataDir = os.getenv("APPDATA") + "\RenPy\Monika After Story"
        else:
            dataDir = "/storage/emulated/0/Android/data/and.kne.masmobile/files/saves"
        
        os.rename(dataDir + "\persistent",dataDir + "\persistent")
        uploadfile(ftp,"persistent" ,dataDir + "\persistent")
        os.rename(dataDir + "\persistent",dataDir + "\persistent")
    
        try:
            ftp.delete(m_name + p_name)
        except Exception as e:
            pass
        ftp.rename("persistent", m_name + "_" + p_name)
        ftp.quit()
        persistent.CloudBackupLastTime = [datetime.date.today(), datetime.datetime.today()]
        return True
    
    def downloadSave():
        ftp = ftpconnect("mas.backup.0721play.icu", 21, "mas_backup_0721play_icu", "3RNNNwYYetBi3LHw")
        if not renpy.android:
            dataDir = renpy.config.basedir + "/characters"
        else:
            dataDir = "/storage/emulated/0/MAS/characters"

        downloadfile(ftp, m_name + "_" + p_name, dataDir + "\persistent")
        ftp.quit()
        return True
        
    try:
        if submods_dp_CloudBackup:
            if datetime.date.today() != persistent.CloudBackupLastTime[0]:
                uploadSave()       
    except:
        pass

screen dp_cloudSetting():
    python:
        submods_screen_dp = store.renpy.get_screen("submods", "screens").scope["tooltip"]
        
    key "noshift_T" action NullAction()
    key "noshift_t" action NullAction()
    key "noshift_M" action NullAction()
    key "noshift_m" action NullAction()
    key "noshift_P" action NullAction()
    key "noshift_p" action NullAction()
    key "noshift_E" action NullAction()
    key "noshift_e" action NullAction()

    modal True

    zorder 200

    style_prefix "confirm"
    add mas_getTimeFile("gui/overlay/confirm.png")

    frame:
        vbox:
            ymaximum 300
            xmaximum 800
            xfill True
            yfill False
            spacing 5

            viewport:
                id "viewport"
                scrollbars "vertical"
                ymaximum 250
                xmaximum 780
                xfill True
                yfill False
                mousewheel True
                
                vbox:
                    xmaximum 780
                    xfill True
                    yfill False
                    box_wrap False

                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        text "每天第一次启动时即会进行一次自动备份. 下载的存档文件位于[renpy.config.basedir]/characters文件夹.\n文件在服务器以'[m_name]_[player]'命名, 请注意是否和其他人重复:)"
                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        textbutton "立刻备份":
                            action Function(uploadSave)
                        textbutton "下载备份":
                            action Function(downloadSave)


          
            hbox:           
                xalign 0.5
                spacing 100
                textbutton "关闭":
                    action Hide("dp_cloudSetting")

init -990 python:
    import os
    if not os.path.exists(renpy.config.basedir + "/game/Submods/dialogue_pack_head.rpy"):
        store.mas_submod_utils.Submod(
            author="P",
            name="云端备份",
            description="安装本模组, 即表示你接受将存档文件上传至mas.backup.0721play.icu.\n自动备份依赖于话题整合包(1.14+), 安装它来获取完整功能",
            version='0.0.1',
            settings_pane="cloudBackup_settingpane"
        )
screen cloudBackup_settingpane():
    vbox:
        xmaximum 800
        xfill True
        style_prefix "check"

        if persistent.submods_dp_gameStatus:
            textbutton ">打开菜单":
                ypos 1
                selected False
                action Show("dp_cloudSetting")
    