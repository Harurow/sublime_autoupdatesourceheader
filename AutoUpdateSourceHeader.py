# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
import re
import os
import fnmatch
from datetime import *

class AutoUpdateSourceHeaderCommand(sublime_plugin.TextCommand):
	__year_pattern1 = "^([0-9]{4}\\s*-\\s*)([0-9]{4})";
	__year_pattern2 = "^([0-9]{4})";

	def update_copyright(self, edit, copyright, region, today):
		if copyright["enable"] == False:
			return False;

		line = self.view.substr(region);

		for p in copyright["patterns"]:
			m = re.search(p, line);
			if not m:
				continue;

			# 'Copyright' matched. search 'Year'.
			offset = region.a + m.end(0);
			sub = m.string[m.end(0):];
			m = re.search(self.__year_pattern1, sub);
			if m:
				# matched XXXX-YYYY
				if m.group(2) != str(today.year):
					# update 'Year'. XXXX-<Year>
					span = m.span(2);
					rgn = sublime.Region(offset + span[0], offset + span[1]);
					old_year = self.view.substr(rgn);
					new_year = str(today.year);
					print ("AutoUpdateSourceHeader - copyright:"
						+ old_year + " > " + new_year);
					self.view.replace(edit, rgn, new_year);
				return True;

			m = re.search(self.__year_pattern2, sub);
			if m:
				# matched XXXX
				if m.group(1) != str(today.year):
					# update 'Year'. XXXX-<Year>
					span = m.span(1);
					rgn = sublime.Region(offset + span[0], offset + span[1]);
					old_year = self.view.substr(rgn);
					new_year = m.group(1) + "-" + str(today.year);
					print ("AutoUpdateSourceHeader - copyright:"
						+ old_year + " > " + new_year);
					self.view.replace(edit, rgn, new_year);
				return True;

		return False;

	def update_modified_user_name(self, edit, user_name, region, my_name):
		if user_name["enable"] == False:
			return False;

		line = self.view.substr(region);

		for p in user_name["patterns"]:
			m = re.search(p, line);
			if not m:
				continue;
			# 'UserName' matched
			offset = region.a + m.end(0);
			sub = m.string[m.end(0):];
			rgn = sublime.Region(offset, offset + len(sub));
			print ("AutoUpdateSourceHeader - modified_user_name:"
				+ self.view.substr(rgn) + " > " + my_name);
			self.view.replace(edit, rgn, my_name);
			return True;

		return False;

	def update_modified_date(self, edit, update_date, region, today):
		if update_date["enable"] == False:
			return False;

		line = self.view.substr(region);

		for p in update_date["patterns"]:
			m = re.search(p, line);
			if not m:
				continue;
			# 'Date' matched
			date_str = today.strftime(update_date["format"]);

			offset = region.a + m.end(0);
			sub = m.string[m.end(0):];
			rgn = sublime.Region(offset, offset + len(sub));
			print ("AutoUpdateSourceHeader - modified_date:"
				+ self.view.substr(rgn) + " > " + date_str);
			self.view.replace(edit, rgn, date_str);
			return True;

		return False;

	def run(self, edit):
		settings = sublime.load_settings("AutoUpdateSourceHeader.sublime-settings");
		analize_lines = settings.get("analize_lines");
		my_name = settings.get("my_name");
		file_exclude_patterns = settings.get("file_exclude_patterns");
		file_include_patterns = settings.get("file_include_patterns");
		copyright = settings.get("copyright");
		modified_user_name = settings.get("modified_user_name");
		modified_date = settings.get("modified_date");

		match_file = False;
		file_name = self.view.file_name();
		if not file_name:
			return;

		file_name = os.path.basename(file_name);

		for fep in file_exclude_patterns:
			if fnmatch.fnmatch(file_name, fep):
				# matched exclude patterns
				print ("exclude patterns matched : " + file_name);
				return;

		for fip in file_include_patterns:
			if fnmatch.fnmatch(file_name, fip):
				# matched include patterns
				match_file = True;
				print ("include patterns matched : " + file_name);
				break;

		if match_file == False:
			return;

		cnt = 1 if copyright["enable"] else 0;
		cnt += 1 if modified_user_name["enable"] else 0;
		cnt += 1 if modified_date["enable"] else 0;
		if cnt == 0:
			return;

		today = datetime.today();

		size = self.view.size();
		for i in range(analize_lines):
			pt = self.view.text_point(i, 0);
			if pt == size:
				break;

			region = self.view.line(pt);

			if self.update_copyright(edit, copyright, region, today):
				copyright["enable"] = False;
				cnt -= 1;
				
			if self.update_modified_user_name(edit, modified_user_name, region, my_name):
				modified_user_name["enable"] = False;
				cnt -= 1;
				
			if self.update_modified_date(edit, modified_date, region, today):
				modified_date["enable"] = False;
				cnt -= 1;

			if cnt == 0:
				break;

class UpdateSourceHeader(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		if view.is_dirty():
			view.run_command("auto_update_source_header");

