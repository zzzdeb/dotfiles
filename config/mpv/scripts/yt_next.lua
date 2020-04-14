local utils = require 'mp.utils'
local ytdlPath = mp.find_config_file("youtube-dl")
local fileDuration = 0
-- Log function: log to both terminal and MPV OSD (On-Screen Display)
function log(string, secs)
    secs = secs or 2.5  -- secs defaults to 2.5 when secs parameter is absent
    mp.msg.warn(string)          -- This logs to the terminal
    mp.osd_message(string, secs) -- This logs to MPV screen
end
local function check_position()
  if fileDuration==0 then
    mp.unobserve_property(check_position)
    return
  end
  local demuxEndPosition = mp.get_property("demuxer-cache-time")
  if demuxEndPosition and 
    fileDuration > 0 and 
    (fileDuration - demuxEndPosition < 1000) and 
    (mp.get_property("playlist-pos-1")==mp.get_property("playlist-count")) then
    local file = mp.get_property("path")
    -- local file = mp.get_property("playlist/"..tostring(next).."/filename")
    local table = { name = "subprocess", args = { "/home/zzz/.scripts/tools/youtube_next_list.sh", file }, capture_stdout=true}
    local result = mp.command_native_async(table,
    function(res, val, err)
        -- print("done subprocess: " .. join(" ", {res, val, err}))
        if res then
            for s in val.stdout:gmatch("[^\r\n]+") do
              -- local ytdl = {}
              -- ytdl.args = {"youtube-dl", "-f "..mp.get_property("ytdl-format"), "-e", s}
              -- local titel = utils.subprocess(ytdl)
              mp.commandv("loadfile", s, "append-play")
            end
        else
            mp.osd_message('Error ' .. tostring(err), 9) -- This logs to MPV screen
        end
    end)
    -- ytdl.args = {ytdlPath, "-f "..mp.get_property("ytdl-format"), "-e", "-g", nextFile}
    -- local res = utils.subprocess(ytdl)
    -- local lines = {}
    -- for s in res.stdout:gmatch("[^\r\n]+") do
      -- table.insert(lines, s)
    -- end
    -- local audioURL = ""
    -- if lines[3] then
      -- audioURL = ',audio-file=['..lines[3]..']'
    -- end
    -- if lines[1] and lines[2] then
      -- mp.commandv("loadfile", lines[2], "append", 'force-media-title=['..lines[1]..']'..audioURL)
      -- mp.commandv("playlist_move", mp.get_property("playlist-count") - 1 , next)
      -- mp.commandv("playlist_remove", next + 1)
    -- end
    mp.unobserve_property(check_position)
  end
end
local function observe()
  if mp.get_property("path"):find("://", 0, false) then
    fileDuration = mp.get_property("duration", 0)
    fileDuration = tonumber(fileDuration)
    mp.observe_property("time-pos", "native", check_position)
  end
end
mp.register_event("file-loaded", observe)
