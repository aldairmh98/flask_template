import configparser

class ConfigReader:
    
    _cfg = None
    instance = None
    _mapped_config = {}

    def __init__(self):
        if ConfigReader.instance is not None:
            raise Exception('Use getInstance')
        ConfigReader.instance = self

    def __env_to_tuple(self, cfg: configparser.ConfigParser):
        for section in cfg.sections():
            self._mapped_config[section] = {}
            for item in cfg.items(section):
                self._mapped_config[section][item[0]] = item[1]
        return
    
    def get_config(self,section, name):
        return self._mapped_config[section][name]

    def get_dict_by_section(self, section):
        return self._mapped_config[section]

    @staticmethod
    def create():
        if ConfigReader.instance is not None:
            return ConfigReader.instance
        ConfigReader._cfg = configparser.ConfigParser()
        ConfigReader._cfg.read('env.ini')
        ConfigReader.instance = ConfigReader()
        ConfigReader.instance.__env_to_tuple(ConfigReader._cfg)
        return ConfigReader.instance
    
