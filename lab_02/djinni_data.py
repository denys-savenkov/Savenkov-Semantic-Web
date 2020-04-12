import xml.etree.ElementTree as ET


class DjinniData:

    def load_xml(self, xml_file):
        self.tree = ET.parse(xml_file)  # get DOM
        self.root = self.tree.getroot()
        return self

    def save_xml(self, xml_file):
        self.tree.write(xml_file, encoding="UTF-8", xml_declaration=True)

    def _add_locations_quantity_attribute(self):
        for location in self.root.iter("locations"):
            location.set("quantity", str(len(location)))

    def _remove_dollars(self):
        for salary in self.root.iter("salary"):
            salary.text = salary.text[1:]

    def _round_years(self):
        for years_of_experience in self.root.iter("years_of_experience"):
            years_of_experience.text = str(int(float(years_of_experience.text)))

    def _extract_skills(self):
        for skills in self.root.iter("skills"):
            skill_list = skills.text.split(', ') if skills.text else []
            skills.text = None
            for skill in skill_list:
                new_skill = ET.SubElement(skills, 'value')
                new_skill.text = skill
            skills.set("quantity", str(len(skill_list)))

    def _add_candidate_ids(self):
        for id, candidate in enumerate(self.root):
            candidate.set("id", str(id))

    def modify(self):
        # task 1 - round_years, remove_dollars (2)
        # task 2 - add_candidate_ids, add_locations_quantity_attribute, extract_skills (3)
        # task 3 -extract_skills (1)
        self._add_candidate_ids()  #
        self._add_locations_quantity_attribute()
        self._remove_dollars()
        self._round_years()
        self._extract_skills()
        return self

    def show(self):
        for candidate in self.root:
            text = f"{candidate.tag} {candidate.attrib} {str(candidate.text)[:10] + '...' if candidate.text is not None else ''}"
            for candidate_info in candidate:
                text += f"\n\t{candidate_info.tag} {candidate_info.attrib} " \
                        f"{str(candidate_info.text)[:10] + '...' if candidate_info.text is not None else ''}"
                for child in candidate_info:
                    text += f"\n\t\t{child.tag} {child.attrib} {child.text}"
            print(text)


djinni_data = DjinniData().load_xml('djinni.xml')
djinni_data.modify().show()
djinni_data.save_xml('new_djinni.xml')
