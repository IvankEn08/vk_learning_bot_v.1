# настройки вк

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api import VkUpload

token = "vk1.a.cDOSna7FDXFQt6rIKbK1vzZ3fp_sLtiNRS5f2kCffd9e_na1NNlNr9aUyI7j0BZObZ3L_HprlSCdJa0jf--dUK4YARP0HtqC1kPgIIP3bAHKqp0k9L67fbQ6zq7J9MKsEJYCQNSwXREKAv3ixlDdhz60e-z9nvYN0wtgDkplXnSx85jyinrdAAGzKvPa-24uPJCRc_495tOeQuX0Y1sptw"

vk = vk_api.VkApi(token=token)
vkapi = vk_api.VkApi(token=token).get_api()
longpoll = VkLongPoll(vk)
upload = VkUpload(vk)
VkEventType = VkEventType
get_random_id = get_random_id