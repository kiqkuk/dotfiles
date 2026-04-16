# custom config.py for qutebrowser
# author: kiqkuk
#
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

import os

# bug video flicker
os.environ["QTWEBENGINE_FORCE_USE_GBM"] = "0"

# Change the argument to True to still load settings configured via autoconfig.yml
config.load_autoconfig(False)

# Additional arguments to pass to Qt, without leading `--`. With
# QtWebEngine, some Chromium arguments (see
# https://peter.sh/experiments/chromium-command-line-switches/ for a
# list) will work.
# Type: List of String
c.qt.args = ['force-dark-mode']

# Force software rendering for QtWebEngine. This is needed for
# QtWebEngine to work with Nouveau drivers and can be useful in other
# scenarios related to graphic issues.
# Type: String
# Valid values:
#   - software-opengl: Tell LibGL to use a software implementation of GL (`LIBGL_ALWAYS_SOFTWARE` / `QT_XCB_FORCE_SOFTWARE_OPENGL`)
#   - qt-quick: Tell Qt Quick to use a software renderer instead of OpenGL. (`QT_QUICK_BACKEND=software`)
#   - chromium: Tell Chromium to disable GPU support and use Skia software rendering instead. (`--disable-gpu`)
#   - none: Don't force software rendering.
c.qt.force_software_rendering = 'none'

# Disable accelerated 2d canvas to avoid graphical glitches. On some
# setups graphical issues can occur on sites like Google sheets and
# PDF.js. These don't occur when accelerated 2d canvas is turned off, so
# we do that by default. So far these glitches only occur on some Intel
# graphics devices.
# Type: String
# Valid values:
#   - always: Disable accelerated 2d canvas
#   - auto: Disable on Qt versions with known issues, enable otherwise
#   - never: Enable accelerated 2d canvas
c.qt.workarounds.disable_accelerated_2d_canvas = 'auto'

# Disable the Hangouts extension. The Hangouts extension provides
# additional APIs for Google domains only. Hangouts has been replaced
# with Meet, which appears to work without this extension. Note this
# setting gets ignored and the Hangouts extension is always disabled to
# avoid crashes on Qt 6.5.0 to 6.5.3 if dark mode is enabled, as well as
# on Qt 6.6.0 and Qt 6.11.0.
# Type: Bool
c.qt.workarounds.disable_hangouts_extension = True

# Always restore open sites when qutebrowser is reopened. Without this
# option set, `:wq` (`:quit --save`) needs to be used to save open tabs
# (and restore them), while quitting qutebrowser in any other way will
# not save/restore the session. By default, this will save to the
# session which was last loaded. This behavior can be customized via the
# `session.default_name` setting.
# Type: Bool
c.auto_save.session = True

# Allow websites to read canvas elements. Note this is needed for some
# websites to work properly. On QtWebEngine < 6.6, this setting requires
# a restart and does not support URL patterns, only the global setting
# is applied.
# Type: Bool
c.content.canvas_reading = False

# Which cookies to accept. With QtWebEngine, this setting also controls
# other features with tracking capabilities similar to those of cookies;
# including IndexedDB, DOM storage, filesystem API, service workers, and
# AppCache. Note that with QtWebKit, only `all` and `never` are
# supported as per-domain values. Setting `no-3rdparty` or `no-
# unknown-3rdparty` per-domain on QtWebKit will have the same effect as
# `all`. If this setting is used with URL patterns, the pattern gets
# applied to the origin/first party URL of the page making the request,
# not the request URL. With QtWebEngine 5.15.0+, paths will be stripped
# from URLs, so URL patterns using paths will not match. With
# QtWebEngine 5.15.2+, subdomains are additionally stripped as well, so
# you will typically need to set this setting for `example.com` when the
# cookie is set on `somesubdomain.example.com` for it to work properly.
# To debug issues with this setting, start qutebrowser with `--debug
# --logfilter network --debug-flag log-cookies` which will show all
# cookies being set.
# Type: String
# Valid values:
#   - all: Accept all cookies.
#   - no-3rdparty: Accept cookies from the same origin only. This is known to break some sites, such as GMail.
#   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain. On QtWebEngine, this is the same as no-3rdparty.
#   - never: Don't accept cookies at all.
c.content.cookies.accept = 'no-3rdparty'

# Allow websites to request geolocations.
# Type: BoolAsk
# Valid values:
#   - true
#   - false
#   - ask
c.content.geolocation = False

# When to send the Referer header. The Referer header tells websites
# from which website you were coming from when visiting them. Note that
# with QtWebEngine, websites can override this preference by setting the
# `Referrer-Policy:` header, so that any websites visited from them get
# the full referer. No restart is needed with QtWebKit.
# Type: String
# Valid values:
#   - always: Always send the Referer. With QtWebEngine 6.2+, this value is unavailable and will act like `same-domain`.
#   - never: Never send the Referer. This is not recommended, as some sites may break.
#   - same-domain: Only send the Referer for the same domain. This will still protect your privacy, but shouldn't break any sites. With QtWebEngine, the referer will still be sent for other domains, but with stripped path information.
c.content.headers.referer = 'same-domain'

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{upstream_browser_version_short}`: The
# corresponding Safari/Chrome   version, but only with its major
# version. * `{qutebrowser_version}`: The currently running qutebrowser
# version.  The default value is equal to the default user agent of
# QtWebKit/QtWebEngine, but with the `QtWebEngine/...` part removed for
# increased compatibility.  Note that the value read from JavaScript is
# always the global value.
# Type: FormatString
c.content.headers.user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'

# List of URLs to ABP-style adblocking rulesets.  Only used when Brave's
# ABP-style adblocker is used (see `content.blocking.method`).  You can
# find an overview of available lists here:
# https://adblockplus.org/en/subscriptions - note that the special
# `subscribe.adblockplus.org` links aren't handled by qutebrowser, you
# will instead need to find the link to the raw `.txt` file (e.g. by
# extracting it from the `location` parameter of the subscribe URL and
# URL-decoding it).
# Type: List of Url
c.content.blocking.method = 'both'
c.content.blocking.adblock.lists = [
         "https://easylist.to/easylist/easylist.txt",
         "https://easylist.to/easylist/easyprivacy.txt",
         "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/filters.txt",
         "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/annoyances.txt",
         "https://raw.githubusercontent.com/uBlockOrigin/uAssets/master/filters/resource-abuse.txt",
]

# Enable WebGL.
# Type: Bool
c.content.webgl = True

# Which interfaces to expose via WebRTC.
# Type: String
# Valid values:
#   - all-interfaces: WebRTC has the right to enumerate all interfaces and bind them to discover public interfaces.
#   - default-public-and-private-interfaces: WebRTC should only use the default route used by http. This also exposes the associated default private address. Default route is the route chosen by the OS on a multi-homed endpoint.
#   - default-public-interface-only: WebRTC should only use the default route used by http. This doesn't expose any local addresses.
#   - disable-non-proxied-udp: WebRTC should only use TCP to contact peers or servers unless the proxy server supports UDP. This doesn't expose any local addresses either.
c.content.webrtc_ip_handling_policy = 'default-public-interface-only'

# Height (in pixels or as percentage of the window) of the completion.
# Type: PercOrInt
c.completion.height = '30%'

# Number of URLs to show in the web history. 0: no history / -1:
# unlimited
# Type: Int
c.completion.web_history.max_items = 1000

# Where to show the downloaded files.
# Type: VerticalPosition
# Valid values:
#   - top
#   - bottom
c.downloads.position = 'bottom'

# Editor (and arguments) to use for the `edit-*` commands. The following
# placeholders are defined:  * `{file}`: Filename of the file to be
# edited. * `{line}`: Line in which the caret is found in the text. *
# `{column}`: Column in which the caret is found in the text. *
# `{line0}`: Same as `{line}`, but starting from index 0. * `{column0}`:
# Same as `{column}`, but starting from index 0.
# Type: ShellCommand
c.editor.command = ['foot', '-e', 'nvim', '{file}', '+{line}']

# Handler for selecting file(s) in forms. If `external`, then the
# commands specified by `fileselect.single_file.command`,
# `fileselect.multiple_files.command` and `fileselect.folder.command`
# are used to select one file, multiple files, and folders,
# respectively.
# Type: String
# Valid values:
#   - default: Use the default file selector.
#   - external: Use an external command.
c.fileselect.handler = 'default'

# CSS border value for hints.
# Type: String
c.hints.border = '1px solid #f9e2af'

# When/how to show the scrollbar.
# Type: String
# Valid values:
#   - always: Always show the scrollbar.
#   - never: Never show the scrollbar.
#   - when-searching: Show the scrollbar when searching for text in the webpage. With the QtWebKit backend, this is equal to `never`.
#   - overlay: Show an overlay scrollbar. On macOS, this is unavailable and equal to `when-searching`; with the QtWebKit backend, this is equal to `never`. Enabling/disabling overlay scrollbars requires a restart.
c.scrolling.bar = 'never'

# When to show the statusbar.
# Type: String
# Valid values:
#   - always: Always show the statusbar.
#   - never: Always hide the statusbar.
#   - in-mode: Show the statusbar when in modes other than normal mode.
c.statusbar.show = 'in-mode'

# Padding (in pixels) around text for tabs.
# Type: Padding
c.tabs.padding = {'bottom': 5, 'left': 9, 'right': 9, 'top': 5}

# Which tab to select when the focused tab is removed.
# Type: SelectOnRemove
# Valid values:
#   - prev: Select the tab which came before the closed one (left in horizontal, above in vertical).
#   - next: Select the tab which came after the closed one (right in horizontal, below in vertical).
#   - last-used: Select the previously selected tab.
c.tabs.select_on_remove = 'next'

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'multiple'

# Format to use for the tab title. The following placeholders are
# defined:  * `{perc}`: Percentage as a string like `[10%]`. *
# `{perc_raw}`: Raw percentage, e.g. `10`. * `{current_title}`: Title of
# the current web page. * `{title_sep}`: The string `" - "` if a title
# is set, empty otherwise. * `{index}`: Index of this tab. *
# `{aligned_index}`: Index of this tab padded with spaces to have the
# same   width. * `{relative_index}`: Index of this tab relative to the
# current tab. * `{id}`: Internal tab ID of this tab. * `{scroll_pos}`:
# Page scroll position. * `{host}`: Host of the current web page. *
# `{backend}`: Either `webkit` or `webengine` * `{private}`: Indicates
# when private mode is enabled. * `{current_url}`: URL of the current
# web page. * `{protocol}`: Protocol (http/https/...) of the current web
# page. * `{audio}`: Indicator for audio/mute status.
# Type: FormatString
c.tabs.title.format = '{audio}{current_title}'

# Width (in pixels or as percentage of the window) of the tab bar if
# it's vertical.
# Type: PercOrInt
c.tabs.width = '7%'

# Width (in pixels) of the progress indicator (0 to disable).
# Type: Int
c.tabs.indicator.width = 0

# Page to open if :open -t/-b/-w is used without URL. Use `about:blank`
# for a blank page.
# Type: FuzzyUrl
c.url.default_page = 'https://github.com/kiqkuk'

# Search engines which can be used via the address bar.  Maps a search
# engine name (such as `DEFAULT`, or `ddg`) to a URL with a `{}`
# placeholder. The placeholder will be replaced by the search term, use
# `{{` and `}}` for literal `{`/`}` braces.  The following further
# placeholds are defined to configure how special characters in the
# search terms are replaced by safe characters (called 'quoting'):  *
# `{}` and `{semiquoted}` quote everything except slashes; this is the
# most   sensible choice for almost all search engines (for the search
# term   `slash/and&amp` this placeholder expands to `slash/and%26amp`).
# * `{quoted}` quotes all characters (for `slash/and&amp` this
# placeholder   expands to `slash%2Fand%26amp`). * `{unquoted}` quotes
# nothing (for `slash/and&amp` this placeholder   expands to
# `slash/and&amp`). * `{0}` means the same as `{}`, but can be used
# multiple times.  The search engine named `DEFAULT` is used when
# `url.auto_search` is turned on and something else than a URL was
# entered to be opened. Other search engines can be used by prepending
# the search engine name to the search term, e.g. `:open google
# qutebrowser`.
# Type: Dict
c.url.searchengines = {'!yt': 'https://www.youtube.com/results?search_query={}', 'DEFAULT': 'https://duckduckgo.com/?q={}'}

# Page(s) to open at the start.
# Type: List of FuzzyUrl, or FuzzyUrl
c.url.start_pages = 'https://duckduckgo.com'

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
# Type: List of QtColor, or QtColor
c.colors.completion.fg = '#a6adc8'

# Background color of the completion widget for odd rows.
# Type: QssColor
c.colors.completion.odd.bg = '#1e1e2e'

# Background color of the completion widget for even rows.
# Type: QssColor
c.colors.completion.even.bg = '#181825'

# Foreground color of completion widget category headers.
# Type: QtColor
c.colors.completion.category.fg = '#cdd6f4'

# Background color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.bg = '#11111b'

# Top border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.top = '#11111b'

# Bottom border color of the completion widget category headers.
# Type: QssColor
c.colors.completion.category.border.bottom = '#11111b'

# Foreground color of the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.fg = '#cdd6f4'

# Background color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.bg = '#45475a'

# Top border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.top = '#45475a'

# Bottom border color of the selected completion item.
# Type: QssColor
c.colors.completion.item.selected.border.bottom = '#45475a'

# Foreground color of the matched text in the selected completion item.
# Type: QtColor
c.colors.completion.item.selected.match.fg = '#fab387'

# Foreground color of the matched text in the completion.
# Type: QtColor
c.colors.completion.match.fg = '#fab387'

# Color of the scrollbar handle in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.fg = '#cba6f7'

# Color of the scrollbar in the completion view.
# Type: QssColor
c.colors.completion.scrollbar.bg = '#11111b'

# Background color of tooltips. If set to null, the Qt default is used.
# Type: QssColor
c.colors.tooltip.bg = '#1e1e2e'

# Foreground color of tooltips. If set to null, the Qt default is used.
# Type: QssColor
c.colors.tooltip.fg = '#cdd6f4'

# Background color of the context menu. If set to null, the Qt default
# is used.
# Type: QssColor
c.colors.contextmenu.menu.bg = '#313244'

# Foreground color of the context menu. If set to null, the Qt default
# is used.
# Type: QssColor
c.colors.contextmenu.menu.fg = '#bac2de'

# Background color of the context menu's selected item. If set to null,
# the Qt default is used.
# Type: QssColor
c.colors.contextmenu.selected.bg = '#585b70'

# Foreground color of the context menu's selected item. If set to null,
# the Qt default is used.
# Type: QssColor
c.colors.contextmenu.selected.fg = '#cdd6f4'

# Background color of disabled items in the context menu. If set to
# null, the Qt default is used.
# Type: QssColor
c.colors.contextmenu.disabled.bg = '#1e1e2e'

# Foreground color of disabled items in the context menu. If set to
# null, the Qt default is used.
# Type: QssColor
c.colors.contextmenu.disabled.fg = '#585b70'

# Background color for the download bar.
# Type: QssColor
c.colors.downloads.bar.bg = '#1e1e2e'

# Color gradient start for download text.
# Type: QtColor
c.colors.downloads.start.fg = '#89b4fa'

# Color gradient start for download backgrounds.
# Type: QtColor
c.colors.downloads.start.bg = '#1e1e2e'

# Color gradient end for download text.
# Type: QtColor
c.colors.downloads.stop.fg = '#a6e3a1'

# Color gradient stop for download backgrounds.
# Type: QtColor
c.colors.downloads.stop.bg = '#1e1e2e'

# Color gradient interpolation system for download text.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.downloads.system.fg = 'none'

# Color gradient interpolation system for download backgrounds.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'none'

# Foreground color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.fg = '#f38ba8'

# Background color for downloads with errors.
# Type: QtColor
c.colors.downloads.error.bg = '#1e1e2e'

# Font color for hints.
# Type: QssColor
c.colors.hints.fg = '#1e1e2e'

# Background color for hints. Note that you can use a `rgba(...)` value
# for transparency.
# Type: QssColor
c.colors.hints.bg = '#fab387'

# Font color for the matched part of hints.
# Type: QtColor
c.colors.hints.match.fg = '#f9e2af'

# Text color for the keyhint widget.
# Type: QssColor
c.colors.keyhint.fg = '#fab387'

# Highlight color for keys to complete the current keychain.
# Type: QssColor
c.colors.keyhint.suffix.fg = '#cba6f7'

# Background color of the keyhint widget.
# Type: QssColor
c.colors.keyhint.bg = '#1e1e2e'

# Foreground color of an error message.
# Type: QssColor
c.colors.messages.error.fg = '#1e1e2e'

# Background color of an error message.
# Type: QssColor
c.colors.messages.error.bg = '#f38ba8'

# Border color of an error message.
# Type: QssColor
c.colors.messages.error.border = '#1e1e2e'

# Foreground color of a warning message.
# Type: QssColor
c.colors.messages.warning.fg = '#1e1e2e'

# Background color of a warning message.
# Type: QssColor
c.colors.messages.warning.bg = '#f9e2af'

# Border color of a warning message.
# Type: QssColor
c.colors.messages.warning.border = '#1e1e2e'

# Foreground color of an info message.
# Type: QssColor
c.colors.messages.info.fg = '#cdd6f4'

# Background color of an info message.
# Type: QssColor
c.colors.messages.info.bg = '#1e1e2e'

# Border color of an info message.
# Type: QssColor
c.colors.messages.info.border = '#cba6f7'

# Foreground color for prompts.
# Type: QssColor
c.colors.prompts.fg = '#bac2de'

# Border used around UI elements in prompts.
# Type: String
c.colors.prompts.border = '1px solid #cba6f7'

# Background color for prompts.
# Type: QssColor
c.colors.prompts.bg = '#1e1e2e'

# Foreground color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.fg = '#cdd6f4'

# Background color for the selected item in filename prompts.
# Type: QssColor
c.colors.prompts.selected.bg = '#181825'

# Foreground color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.fg = '#cdd6f4'

# Background color of the statusbar.
# Type: QssColor
c.colors.statusbar.normal.bg = '#1e1e2e'

# Foreground color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.fg = '#a6e3a1'

# Background color of the statusbar in insert mode.
# Type: QssColor
c.colors.statusbar.insert.bg = '#11111b'

# Foreground color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.fg = '#11111b'

# Background color of the statusbar in passthrough mode.
# Type: QssColor
c.colors.statusbar.passthrough.bg = '#89b4fa'

# Foreground color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.fg = '#cdd6f4'

# Background color of the statusbar in private browsing mode.
# Type: QssColor
c.colors.statusbar.private.bg = '#45475a'

# Foreground color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.fg = '#cdd6f4'

# Background color of the statusbar in command mode.
# Type: QssColor
c.colors.statusbar.command.bg = '#11111b'

# Foreground color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.fg = '#cba6f7'

# Background color of the statusbar in private browsing + command mode.
# Type: QssColor
c.colors.statusbar.command.private.bg = '#11111b'

# Foreground color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.fg = '#fab387'

# Background color of the statusbar in caret mode.
# Type: QssColor
c.colors.statusbar.caret.bg = '#11111b'

# Foreground color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.fg = '#1e1e2e'

# Background color of the statusbar in caret mode with a selection.
# Type: QssColor
c.colors.statusbar.caret.selection.bg = '#fab387'

# Background color of the progress bar.
# Type: QssColor
c.colors.statusbar.progress.bg = '#cba6f7'

# Default foreground color of the URL in the statusbar.
# Type: QssColor
c.colors.statusbar.url.fg = '#cdd6f4'

# Foreground color of the URL in the statusbar on error.
# Type: QssColor
c.colors.statusbar.url.error.fg = '#f38ba8'

# Foreground color of the URL in the statusbar for hovered links.
# Type: QssColor
c.colors.statusbar.url.hover.fg = '#89b4fa'

# Foreground color of the URL in the statusbar on successful load
# (http).
# Type: QssColor
c.colors.statusbar.url.success.http.fg = '#a6e3a1'

# Foreground color of the URL in the statusbar on successful load
# (https).
# Type: QssColor
c.colors.statusbar.url.success.https.fg = '#a6e3a1'

# Foreground color of the URL in the statusbar when there's a warning.
# Type: QssColor
c.colors.statusbar.url.warn.fg = '#f9e2af'

# Background color of the tab bar.
# Type: QssColor
c.colors.tabs.bar.bg = '#11111b'

# Color gradient start for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.start = '#89b4fa'

# Color gradient end for the tab indicator.
# Type: QtColor
c.colors.tabs.indicator.stop = '#a6e3a1'

# Color for the tab indicator on errors.
# Type: QtColor
c.colors.tabs.indicator.error = '#f38ba8'

# Color gradient interpolation system for the tab indicator.
# Type: ColorSystem
# Valid values:
#   - rgb: Interpolate in the RGB color system.
#   - hsv: Interpolate in the HSV color system.
#   - hsl: Interpolate in the HSL color system.
#   - none: Don't show a gradient.
c.colors.tabs.indicator.system = 'none'

# Foreground color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.fg = '#7f849c'

# Background color of unselected odd tabs.
# Type: QtColor
c.colors.tabs.odd.bg = '#45475a'

# Foreground color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.fg = '#9399b2'

# Background color of unselected even tabs.
# Type: QtColor
c.colors.tabs.even.bg = '#585b70'

# Foreground color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.fg = '#cdd6f4'

# Background color of selected odd tabs.
# Type: QtColor
c.colors.tabs.selected.odd.bg = '#1e1e2e'

# Foreground color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.fg = '#cdd6f4'

# Background color of selected even tabs.
# Type: QtColor
c.colors.tabs.selected.even.bg = '#1e1e2e'

# Foreground color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.fg = '#cdd6f4'

# Background color of pinned unselected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.odd.bg = '#7f849c'

# Foreground color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.fg = '#cdd6f4'

# Background color of pinned unselected even tabs.
# Type: QtColor
c.colors.tabs.pinned.even.bg = '#6c7086'

# Foreground color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.fg = '#cdd6f4'

# Background color of pinned selected odd tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.odd.bg = '#181825'

# Foreground color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.fg = '#cdd6f4'

# Background color of pinned selected even tabs.
# Type: QtColor
c.colors.tabs.pinned.selected.even.bg = '#1e1e2e'

# Background color for webpages if unset (or empty to use the theme's
# color).
# Type: QtColor
c.colors.webpage.bg = None

# Value to use for `prefers-color-scheme:` for websites. The "light"
# value is only available with QtWebEngine 5.15.2+. On older versions,
# it is the same as "auto". The "auto" value is broken on QtWebEngine
# 5.15.2 due to a Qt bug. There, it will fall back to "light"
# unconditionally.
# Type: String
# Valid values:
#   - auto: Use the system-wide color scheme setting.
#   - light: Force a light theme.
#   - dark: Force a dark theme.
c.colors.webpage.preferred_color_scheme = 'dark'

# Render all web contents using a dark theme. On QtWebEngine < 6.7, this
# setting requires a restart and does not support URL patterns, only the
# global setting is applied. Example configurations from Chromium's
# `chrome://flags`: - "With simple HSL/CIELAB/RGB-based inversion": Set
# `colors.webpage.darkmode.algorithm` accordingly, and   set
# `colors.webpage.darkmode.policy.images` to `never`.  - "With selective
# image inversion": qutebrowser default settings.
# Type: Bool
c.colors.webpage.darkmode.enabled = False

# Which images to apply dark mode to.
# Type: String
# Valid values:
#   - always: Apply dark mode filter to all images.
#   - never: Never apply dark mode filter to any images.
#   - smart: Apply dark mode based on image content. Not available with Qt 5.15.0.
#   - smart-simple: On QtWebEngine 6.6, use a simpler algorithm for smart mode (based on numbers of colors and transparency), rather than an ML-based model. Same as 'smart' on older QtWebEnigne versions.
c.colors.webpage.darkmode.policy.images = 'never'

c.downloads.location.directory = '$HOME/down'
